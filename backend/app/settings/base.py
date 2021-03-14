from typing import Optional, cast
from pathlib import Path
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

p: Path = Path(__file__).parents[2] / ".env"
config: Config = Config(p if p.exists() else None)
