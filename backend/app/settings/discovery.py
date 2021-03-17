from typing import Optional, cast
import os
from pathlib import Path
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from .base import config

SAMPLE_SIZE = config("DUCK_DISCOVERY_SAMPLE_SIZE", cast=int, default=5000)
WORKER_COUNT = config("DUCK_DISCOVERY_WORKER_COUNT", cast=int, default=4)

PERSIST_BUFFER_SIZE = config(
    "DUCK_DISCOVERY_PERSIST_BUFFER_SIZE", cast=int, default=10
)
