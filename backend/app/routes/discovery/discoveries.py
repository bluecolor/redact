from sqlalchemy import func
from typing import List, Optional, Union
from arq.connections import ArqRedis
from fastapi import Depends, WebSocket
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import outerjoin
from sqlalchemy.sql.functions import func, mode
from sqlalchemy.orm.exc import NoResultFound
import app.models.orm as models
import app.models.schemas.discovery as s
from .base import router
from app.database import get_db
from app.oracle import redact
from pydantic import parse_obj_as
from arq.connections import ArqRedis, create_pool
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page, Params


@router.get(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{plan_instance_id}/discoveries/group-by-rule",
    tags=["Discoveries"],
    response_model=List[s.DiscoveryGroupByRuleOut],
)
async def get_discoveries_group_by_rule(
    conn_id: int,
    plan_id: int,
    plan_instance_id: int,
    db: Session = Depends(get_db),
):
    disvcoveries = (
        db.query(models.Discovery.rule_id, func.count())
        .outerjoin(models.PlanInstance)
        .outerjoin(models.Plan)
        .filter(
            models.PlanInstance.id == plan_instance_id,
            models.Plan.id == plan_id,
            models.Connection.id == conn_id,
        )
        .group_by(models.Discovery.rule_id)
        .all()
    )

    plan_instance = (
        db.query(models.PlanInstance)
        .outerjoin(models.Plan)
        .outerjoin(models.Connection)
        .filter(
            models.PlanInstance.id == plan_instance_id,
            models.Plan.id == plan_id,
            models.Connection.id == conn_id,
        )
        .one()
    )

    rules = plan_instance.plan.rules
    print(rules)

    def get_rule(id):
        for r in rules:
            if r.id == id:
                return r

    _disvcoveries = [
        s.DiscoveryGroupByRuleOut(rule=get_rule(d[0]), count=d[1])
        for d in disvcoveries
    ]
    return parse_obj_as(List[s.DiscoveryGroupByRuleOut], _disvcoveries)


@router.get(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{plan_instance_id}/rules/{rule_id}/discoveries",
    tags=["Discoveries"],
    response_model=Page[s.DiscoveryOut],
)
async def get_discoveries_for_rule(
    conn_id: int,
    plan_id,
    plan_instance_id: int,
    rule_id: Optional[int] = None,
    db: Session = Depends(get_db),
    params: Params = Depends(),
):
    disvcoveries = (
        db.query(models.Discovery)
        .outerjoin(models.Rule)
        .outerjoin(models.PlanInstance)
        .outerjoin(models.Plan)
        .outerjoin(models.Connection)
        .filter(
            models.Connection.id == conn_id,
            models.Plan.id == plan_id,
            models.PlanInstance.id == plan_instance_id,
            models.Rule.id == rule_id,
        )
    )
    return paginate(disvcoveries, params)


@router.get(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{plan_instance_id}/discoveries",
    tags=["Discoveries"],
    response_model=Page[s.DiscoveryOut],
)
async def get_discoveries(
    conn_id: int,
    plan_id,
    plan_instance_id: int,
    rule_id: Optional[int] = None,
    db: Session = Depends(get_db),
    params: Params = Depends(),
):
    disvcoveries = (
        db.query(models.Discovery)
        .outerjoin(models.Rule)
        .outerjoin(models.PlanInstance)
        .outerjoin(models.Plan)
        .outerjoin(models.Connection)
        .filter(
            models.Connection.id == conn_id,
            models.Plan.id == plan_id,
            models.PlanInstance.id == plan_instance_id,
            models.Rule.id == rule_id if rule_id else True,
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
