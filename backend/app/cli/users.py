from typing import List
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


@click.command("list")
def list():
    for db in get_db():
        users: List[model.User] = db.query(model.User).all()
        for user in users:
            print(f"{user.username} - {user.name}")


@click.group()
def users():
    """User commands"""


users.add_command(add)
users.add_command(list)
