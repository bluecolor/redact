from app.celery import celery_app
from app.redis import redis_conn as redis


@celery_app.task(acks_late=True)
def notify(message: str):
    channel = "notifications"
    redis.publish(channel, message=message)
