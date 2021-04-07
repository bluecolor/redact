from typing import List
import logging
import click

from app.celery import celery_app
from celery.bin import worker as celery_worker


@click.command("worker")
def worker():
    w = celery_worker.worker(app=celery_app)
    w.run(queues="discoveries,notifications")


@click.group()
def celery():
    """Celery related tasks"""


celery.add_command(worker)
