from typing import Optional, cast
import os
from pathlib import Path
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from .base import config

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI", "postgresql://duck:duck@localhost:5432/duck"
)
SQLALCHEMY_TRACK_MODIFICATIONS = (
    os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False").lower() == "true"
)
SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "False").lower() == "true"

FERNET_KEY = os.getenv(
    "DUCK_FERNET_KEY", "ar8tXmAkcaTw9BCowyhh8f5GnRw1AEEzczjwTolnoZ4="
)

