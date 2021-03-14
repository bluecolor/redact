from rq.job import Job
from app.worker import job
from time import sleep


@job("default")
def run():
    print("task started")
    sleep(20)
    print("task ended")
