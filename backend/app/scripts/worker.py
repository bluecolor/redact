import redis
from rq import Worker, Queue, Connection
from app.settings.rq import REDIS_URL, QUEUES

conn = redis.from_url(REDIS_URL)

with Connection(conn):
    worker = Worker(QUEUES)
    worker.work()
