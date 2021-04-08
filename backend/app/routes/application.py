from typing import List, Optional
import pkg_resources
from app.models.schemas import VersionOut
from .base import router


@router.get("/application/version", response_model=VersionOut)
def get_version():
    version = pkg_resources.get_distribution("app").version
    return VersionOut(version=version)

