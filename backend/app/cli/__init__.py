import click
from .users import users


@click.group()
def duck():
    """Duck"""


duck.add_command(users)
