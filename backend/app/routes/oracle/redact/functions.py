from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.oracle.redact as s
from .base import router
from app.database import get_db


@router.get(
    "/oracle/redact/functions/types", response_model=List[s.FunctionTypeOut],
)
def get_types() -> List[s.FunctionTypeOut]:
    return redact.get_function_types()


@router.get(
    "/oracle/redact/functions/parameters",
    response_model=List[s.FunctionParametersOut],
)
def get_parameters():
    return redact.get_function_parameters()


@router.get(
    "/oracle/redact/functions/actions", response_model=List[s.ActionOut],
)
def get_actions() -> List[s.ActionOut]:
    return redact.get_actions()
