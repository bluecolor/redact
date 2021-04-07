from celery import Celery
from app.settings import REDIS_URL

celery_app = Celery("worker", broker=REDIS_URL, backend=REDIS_URL)


celery_app.conf.task_routes = (
    [
        ("app.tasks.discovery.*", {"queue": "discoveries"}),
        ("app.tasks.notification.*", {"queue": "notifications"}),
    ],
)
