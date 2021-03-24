import redis
from app.settings.celery import REDIS_URL

redis_conn = redis.from_url(REDIS_URL)
