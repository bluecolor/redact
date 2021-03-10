from typing import Optional
import os
from pathlib import Path
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

p: Path = Path(__file__).parents[2] / ".env"
config: Config = Config(p if p.exists() else None)

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

REDIS_IP: str = config("REDIS_IP", cast=str, default="127.0.0.1")
REDIS_PORT: int = config("REDIS_PORT", cast=int, default=6379)

ARQ_BACKGROUND_FUNCTIONS: Optional[CommaSeparatedStrings] = config(
    "DUCK_ARQ_BACKGROUND_FUNCTIONS", cast=CommaSeparatedStrings, default=None
)
