import asyncio
from .settings.arq import settings as redis_settings
from arq.connections import ArqRedis, create_pool


redis: ArqRedis = None

async def get_redis_pool() -> ArqRedis:
    global redis
    if redis:
        return redis
    else:
        return await create_pool(redis_settings)

