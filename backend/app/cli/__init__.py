import click
from .users import users
import uvicorn
from app import app
from app.settings import HOST, PORT, LOG_LEVEL
from .celery import celery
from .db import db


@click.group()
def duck():
    """Duck"""


@click.command("hello")
def hello():
    print("Hello back")


@click.command("run")
def run():
    uvicorn.run(app, host=HOST, port=PORT, log_level=LOG_LEVEL)


duck.add_command(db)
duck.add_command(users)
duck.add_command(hello)
duck.add_command(celery)
