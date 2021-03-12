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
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances",
    tags=["PlanInstances"],
    response_model=List[schemas.PlanInstanceOut],
)
async def get_plan_instances(
    conn_id: int, plan_id: int, db: Session = Depends(get_db)
):
    plan_instances = (
        db.query(models.PlanInstance)
        .outerjoin(models.Plan)
        .filter(
            models.Plan.connection_id == conn_id and models.Plan.id == plan_id
        )
        .all()
    )
    return parse_obj_as(List[schemas.PlanInstanceOut], plan_instances)


@router.get(
    "/connections/{conn_id}/discovery/plans/instances",
    tags=["PlanInstances"],
    response_model=List[schemas.PlanInstanceOut],
)
async def get_all_plan_instances(conn_id: int, db: Session = Depends(get_db)):
    plan_instances = (
        db.query(models.PlanInstance)
        .outerjoin(models.Plan)
        .filter(models.Plan.connection_id == conn_id)
        .all()
    )
    return parse_obj_as(List[schemas.PlanInstanceOut], plan_instances)


@router.get(
    "/connections/{conn_id}/discovery/plans/instances/{id}",
    tags=["PlanInstances"],
    response_model=schemas.PlanInstanceOut,
)
async def get_plan_instance(
    conn_id: int, id: int, db: Session = Depends(get_db)
):
    plan_instance = db.query(models.PlanInstance).get(id)
    return schemas.PlanInstanceOut.from_orm(plan_instance)


@router.get(
    "/connections/{conn_id}/discovery/plans/instances/{plan_instance_id}/discoveries",
    tags=["Discoveries"],
    response_model=Union[
        List[schemas.DiscoveryOut], List[schemas.DiscoveryByRuleOut]
    ],
)
async def get_discoveries(
    conn_id: int,
    plan_instance_id: int,
    by_rule: Optional[bool] = False,
    db: Session = Depends(get_db),
):
    if by_rule:
        disvcoveries = (
            db.query(models.Discovery.rule_id, func.count())
            .outerjoin(models.PlanInstance)
            .filter(models.PlanInstance.id == plan_instance_id)
            .group_by(models.Discovery.rule_id)
            .all()
        )
        _disvcoveries = [
            schemas.DiscoveryByRuleOut(rule_id=d[0], count=d[1])
            for d in disvcoveries
        ]
        return parse_obj_as(List[schemas.DiscoveryByRuleOut], _disvcoveries)
    else:
        disvcoveries = (
            db.query(models.Discovery)
            .outerjoin(models.PlanInstance)
            .filter(models.PlanInstance.id == plan_instance_id)
            .all()
        )
        return parse_obj_as(List[schemas.DiscoveryOut], disvcoveries)


@router.get(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{plan_instance_id}/rules/{rule_id}",
    tags=["Discoveries"],
    response_model=Page[schemas.DiscoveryOut],
)
async def get_discoveries_for_rule(
    conn_id: int,
    plan_id,
    plan_instance_id: int,
    rule_id: int,
    db: Session = Depends(get_db),
    params: Params = Depends(),
):
    disvcoveries = (
        db.query(models.Discovery)
        .outerjoin(models.PlanInstance)
        .outerjoin(models.Plan)
        .outerjoin(models.Rule)
        .filter(
            models.Plan.id == plan_id
            and models.PlanInstance.id == plan_instance_id
            and models.Rule.id == rule_id
        )
    )
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
