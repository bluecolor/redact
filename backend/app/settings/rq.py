from .base import config


REDIS_URL: str = config(
    "DUCK_RQ_REDIS_URL", default="redis://localhost:6379/0"
)
QUEUES = ["high", "default", "low"]

