import logging
import click
from app.database import get_db
import app.models.orm as model


logger = logging.getLogger("cli.users")


@click.command("add")
@click.option("-n", "--name", type=str, required=True)
@click.option("-e", "--email", type=str, required=True)
@click.option("-u", "--username", type=str, required=True)
@click.option("-p", "--password", type=str, required=True)
def add(name, email, username, password):
    for db in get_db():
        user: model.User = model.User(
            name=name, email=email, username=username, password=password
        )
        db.add(user)
        db.commit()
        print("User created")


@click.group()
def users():
    """Delete config commands"""


users.add_command(add)