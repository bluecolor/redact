# isort:skip_file

import sys

sys.path.extend(["./"])

from pydantic.utils import import_string

from .database import get_db
from .settings.arq import settings
from .settings.globals import ARQ_BACKGROUND_FUNCTIONS

FUNCTIONS: list = [
    import_string(background_function)
    for background_function in list(ARQ_BACKGROUND_FUNCTIONS)
] if ARQ_BACKGROUND_FUNCTIONS is not None else list()




class WorkerSettings:
    """
    Settings for the ARQ worker.
    """
    redis_settings = settings
    functions: list = FUNCTIONS
