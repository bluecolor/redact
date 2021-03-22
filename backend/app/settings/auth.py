from typing import Optional, cast
import os
from pathlib import Path
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from .base import config


SECRET_KEY = Secret(
    config(
        "DUCK_SECRET_KEY",
        default="361e9e128ac204e66d5bfeca82814626353b96768d9180537aec5fdefc83d32d",
    )
)

JWT_ALGORITHM = config("DUCK_JWT_ALGORITHM", default="HS256",)

ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "DUCK_ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=(7 * 24 * 60),
)
