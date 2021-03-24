from .base import config

REDIS_PUBSUB_TIMEOUT = config(
    "DUCK_REDIS_PUBSUB_TIMEOUT", cast=int, default=2 * 50
)
