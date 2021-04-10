from sqlalchemy import func
from typing import List, Optional, Union
from fastapi import Depends, WebSocket
from starlette.websockets import WebSocketState
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import outerjoin
from sqlalchemy.sql.functions import func, mode
from sqlalchemy.orm.exc import NoResultFound
import app.models.orm as models
import app.models.schemas.discovery as s
from .base import router
from app.database import get_db
from pydantic import parse_obj_as
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page, Params
from app.settings import REDIS_URL, REDIS_PUBSUB_TIMEOUT
import aioredis
import asyncio


@router.get(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{plan_instance_id}/discoveries/group-by-schema",
    tags=["Discoveries"],
    response_model=List[s.DiscoveryGroupBySchemaOut],
)
async def get_discoveries_group_by_schema(
    conn_id: int,
    plan_id: int,
    plan_instance_id: int,
    db: Session = Depends(get_db),
):
    disvcoveries = (
        db.query(models.Discovery.schema_name, func.count())
        .outerjoin(models.PlanInstance)
        .outerjoin(models.Plan)
        .outerjoin(models.Connection)
        .filter(
            models.PlanInstance.id == plan_instance_id,
            models.Plan.id == plan_id,
            models.Connection.id == conn_id,
        )
        .group_by(models.Discovery.schema_name)
        .all()
    )
    _disvcoveries = [
        s.DiscoveryGroupBySchemaOut(schema_name=d[0], count=d[1])
        for d in disvcoveries
    ]
    return parse_obj_as(List[s.DiscoveryGroupBySchemaOut], _disvcoveries)


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


# todo handle client disconnect
@router.websocket(
    "/ws/connections/{conn_id}/discovery/plans/{plan_id}/instances/{plan_instance_id}"
)
async def plan_runs(
    conn_id: int, plan_id: int, plan_instance_id: int, websocket: WebSocket
):
    total_key = f"discovery:search:total:connections:{conn_id}:plans:{plan_id}:instances:{plan_instance_id}"
    progress_key = f"discovery:search:progress:connections:{conn_id}:plans:{plan_id}:instances:{plan_instance_id}"

    await websocket.accept()

    async def reader(ch):
        redis = await aioredis.create_redis(
            REDIS_URL, timeout=REDIS_PUBSUB_TIMEOUT
        )
        total = int(await redis.get(total_key))
        while await ch.wait_message():
            msg = await ch.get_json()
            if msg.get("done"):
                break
            progress = int(await redis.get(progress_key))
            if websocket.client_state == WebSocketState.DISCONNECTED:
                break
            await websocket.send_json(
                {**msg, "total": total, "progress": progress}
            )

    redis = await aioredis.create_redis(
        REDIS_URL, timeout=REDIS_PUBSUB_TIMEOUT
    )
    address = f"discovery:search:connections:{conn_id}:plans:{plan_id}:instances:{plan_instance_id}"
    res = await redis.subscribe(address)
    # await asyncio.ensure_future(reader(res[0]))
    asyncio.create_task(reader(res[0]))

    while True:
        try:
            print(await websocket.receive())
        except Exception:
            break

