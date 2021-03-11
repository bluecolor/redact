from sqlalchemy import func
from typing import List, Optional, Union
from arq.connections import ArqRedis
from fastapi import Depends, WebSocket
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import outerjoin
from sqlalchemy.sql.functions import func, mode
import app.models.orm as models
import app.models.schemas as schemas
from .base import router
from app.database import get_db
from app.oracle import redact
from pydantic import parse_obj_as
from app import get_redis_pool
from app.settings.arq import settings as redis_settings
from arq.connections import ArqRedis, create_pool
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page, Params

@router.get(
    "/connections/{conn_id}/discovery/rules/{id}",
    response_model=schemas.RuleOut,
)
def get_rule( conn_id: int, id: int, db: Session = Depends(get_db)) -> schemas.RuleOut:
    rule = db.query(models.Rule).outerjoin(models.Connection)\
        .filter(models.Connection.id == conn_id and models.Rule.id == id).one()
    return schemas.RuleOut.from_orm(rule)


@router.get(
    "/connections/{conn_id}/discovery/rules",
    response_model=List[schemas.RuleOut],
)
def get_rules(conn_id: int, db: Session = Depends(get_db)) -> List[schemas.RuleOut]:
    rules = db.query(models.Rule).filter(models.Rule.connection_id == conn_id).all()
    return parse_obj_as(List[schemas.RuleOut], rules)


@router.post(
    "/connections/{conn_id}/discovery/rules", tags=["Rules"], response_model=schemas.RuleOut
)
def create_rule(conn_id: int, rule: schemas.RuleCreateIn, db: Session = Depends(get_db)):
    new_rule: models.Rule = models.Rule(**{**rule.dict(), "connection_id": conn_id})
    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)

    return schemas.RuleOut.from_orm(new_rule)


@router.delete("/connections/{conn_id}/discovery/rules/{id}", response_model=schemas.RuleDeleteOut)
def delete_rule(conn_id: int,id: int, db: Session = Depends(get_db)):
    rule = db.query(models.Rule).get(id)
    db.delete(rule)
    db.commit()
    return schemas.RuleDeleteOut.from_orm(rule)


@router.get(
    "/connections/{conn_id}/discovery/plans",
    response_model=List[schemas.PlanOut],
)
def get_plans(conn_id: int, db: Session = Depends(get_db)) -> List[schemas.PlanOut]:
    rules = db.query(models.Plan).filter(models.Plan.connection_id == conn_id).all()
    return parse_obj_as(List[schemas.PlanOut], rules)


@router.post(
    "/connections/{conn_id}/discovery/plans", tags=["Plans"], response_model=schemas.PlanOut
)
def create_plan(conn_id: int, plan: schemas.PlanCreateIn, db: Session = Depends(get_db)):
    rules = db.query(models.Rule).filter(models.Rule.id.in_(plan.rules)).all()
    new_plan: models.Plan = models.Plan(**{**plan.dict(), "connection_id": conn_id, "rules": rules})
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return schemas.PlanOut.from_orm(new_plan)

@router.delete("/connections/{conn_id}/discovery/plans/{id}", response_model=schemas.PlanDeleteOut)
def delete_plan(conn_id: int,id: int, db: Session = Depends(get_db)):
    plan = db.query(models.Plan).get(id)
    db.delete(plan)
    db.commit()
    return schemas.PlanDeleteOut.from_orm(plan)


@router.post(
    "/connections/{conn_id}/discovery/plans/{plan_id}/run", tags=["Plans"]
)
async def run_plan(conn_id: int, plan_id: int, db: Session = Depends(get_db), redis: ArqRedis = Depends(get_redis_pool)):
    job = await redis.enqueue_job(
        "run_plan", conn_id, plan_id
    )
    return job.job_id


@router.get(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances",
    tags=["PlanInstances"],
    response_model=List[schemas.PlanInstanceOut]
)
async def get_plan_instances(conn_id: int, plan_id: int, db: Session = Depends(get_db)):
    plan_instances = db.query(models.PlanInstance)\
        .outerjoin(models.Plan)\
        .filter(models.Plan.connection_id == conn_id and models.Plan.id == plan_id)\
        .all()
    return parse_obj_as(List[schemas.PlanInstanceOut],plan_instances)


@router.get(
    "/connections/{conn_id}/discovery/plans/instances/{id}",
    tags=["PlanInstances"],
    response_model=schemas.PlanInstanceOut
)
async def get_plan_instance(conn_id: int, id: int, db: Session = Depends(get_db)):
    plan_instance = db.query(models.PlanInstance).get(id)
    return schemas.PlanInstanceOut.from_orm(plan_instance)


@router.get(
    "/connections/{conn_id}/discovery/plans/instances/{plan_instance_id}/discoveries",
    tags=["Discoveries"],
    response_model= Union[List[schemas.DiscoveryOut], List[schemas.DiscoveryByRuleOut]]
)
async def get_discoveries(conn_id: int, plan_instance_id: int, by_rule: Optional[bool] = False,  db: Session = Depends(get_db)):
    if by_rule:
        disvcoveries = db.query(models.Discovery.rule_id, func.count())\
            .outerjoin(models.PlanInstance)\
            .filter(models.PlanInstance.id == plan_instance_id)\
            .group_by(models.Discovery.rule_id)\
            .all()
        _disvcoveries = [schemas.DiscoveryByRuleOut(rule_id=d[0], count=d[1]) for d in disvcoveries]
        return parse_obj_as(List[schemas.DiscoveryByRuleOut], _disvcoveries)
    else:
        disvcoveries = db.query(models.Discovery)\
            .outerjoin(models.PlanInstance)\
            .filter(models.PlanInstance.id == plan_instance_id)\
            .all()
        return parse_obj_as(List[schemas.DiscoveryOut], disvcoveries)


@router.get(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{plan_instance_id}/rules/{rule_id}",
    tags=["Discoveries"],
    response_model= Page[schemas.DiscoveryOut]
)
async def get_discoveries_for_rule(
    conn_id: int, plan_id, plan_instance_id: int, rule_id: int,
    db: Session = Depends(get_db),
    params: Params = Depends()
):
    disvcoveries = db.query(models.Discovery)\
            .outerjoin(models.PlanInstance)\
            .outerjoin(models.Plan)\
            .outerjoin(models.Rule)\
            .filter(
                    models.Plan.id == plan_id
                and models.PlanInstance.id == plan_instance_id
                and models.Rule.id == rule_id)
    return paginate(disvcoveries, params)


@router.websocket("/ws/plans/instances")
async def plan_runs(websocket: WebSocket):
    ...
    # await websocket.accept()
    # redis: ArqRedis = await create_pool(redis_settings)
    # res = await redis.subscribe('plan:run')
    # ch = res[0]

    # while (await ch.wait_message()):
    #     msg = await ch.get_json()
    #     print("Got Message:", msg)
    #     await websocket.send_json(msg)
