import click
import uvicorn

from app.main import app
from app.settings import HOST, LOG_LEVEL, PORT

from .celery import celery
from .db import db
from .users import users


@click.group()
def redact():
    """Duck"""


@click.command("hello")
def hello():
    print("Hello back")


@click.command("run")
def run():
    uvicorn.run(app, host=HOST, port=PORT, log_level=LOG_LEVEL)


redact.add_command(run)
redact.add_command(db)
redact.add_command(users)
redact.add_command(hello)
redact.add_command(celery)
