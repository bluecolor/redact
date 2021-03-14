from functools import partial
from rq.decorators import job as rq_job
from . import rq_redis_connection

job = partial(rq_job, connection=rq_redis_connection)
