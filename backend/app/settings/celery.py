from .base import config


REDIS_URL: str = config(
    "DUCK_CELERY_REDIS_URL", default="redis://localhost:6379/0"
)

