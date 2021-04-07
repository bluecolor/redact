from sqlalchemy import func
from typing import List, Optional, Union
from fastapi import Depends, WebSocket
from starlette.websockets import WebSocketState
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func, mode
from sqlalchemy.orm.exc import NoResultFound
import app.models.orm as models
import app.models.schemas.discovery as s
from .base import router
from app.database import get_db
from pydantic import parse_obj_as
from fastapi_pagination.ext.sqlalchemy import paginate
from app.settings import REDIS_URL, REDIS_PUBSUB_TIMEOUT
import aioredis
import asyncio


# todo handle client disconnect
@router.websocket("/ws/notifications")
async def notifications(
    conn_id: Optional[int] = None, websocket: WebSocket = None
):
    await websocket.accept()

    async def reader(ch):
        while await ch.wait_message():
            msg = await ch.get_json()
            if websocket.client_state == WebSocketState.DISCONNECTED:
                break
            await websocket.send_json(msg)

    redis = await aioredis.create_redis(
        REDIS_URL, timeout=REDIS_PUBSUB_TIMEOUT
    )
    res = await redis.subscribe("notifications")
    # await asyncio.ensure_future()
    asyncio.create_task(reader(res[0]))

    while True:
        try:
            print(await websocket.receive())
        except Exception:
            break

