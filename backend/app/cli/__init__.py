import click
import uvicorn

from app.main import app
from app.settings import HOST, LOG_LEVEL, PORT

from .celery import celery
from .db import db
from .users import users


@click.group()
def duck():
    """Duck"""


@click.command("hello")
def hello():
    print("Hello back")


@click.command("run")
def run():
    uvicorn.run(app, host=HOST, port=PORT, log_level=LOG_LEVEL)


duck.add_command(run)
duck.add_command(db)
duck.add_command(users)
duck.add_command(hello)
duck.add_command(celery)
