import click
from .users import users


@click.command("hello")
def hello():
    print("Hello back")


@click.group()
def duck():
    """Duck"""


duck.add_command(users)
duck.add_command(hello)
