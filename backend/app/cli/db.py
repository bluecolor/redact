import os
from typing import List
import logging
import click
from alembic import command
from app.settings import SQLALCHEMY_DATABASE_URI

logger = logging.getLogger("cli.db")


@click.group()
def db():
    """Database commands"""


def _get_alembic_config():
    from alembic.config import Config

    current_dir = os.path.dirname(os.path.abspath(__file__))
    package_dir = os.path.normpath(os.path.join(current_dir, ".."))
    directory = os.path.join(package_dir, "migrations")
    config = Config(os.path.join(package_dir, "alembic.ini"))
    config.set_main_option("script_location", directory.replace("%", "%%"))
    config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URI)
    return config


@click.command("init")
def init():
    config = _get_alembic_config()
    command.upgrade(config, "heads")


db.add_command(init)
