from typing import List
import app.models.schemas.oracle.redact as s
from .base import router
from app.vendors.oracle import Oracle


@router.get(
    "/oracle/redact/functions/types", response_model=List[s.FunctionTypeOut],
)
def get_types() -> List[s.FunctionTypeOut]:
    return Oracle.function_types()


@router.get(
    "/oracle/redact/functions/parameters",
    response_model=List[s.FunctionParametersOut],
)
def get_parameters():
    return Oracle.function_parameters()


@router.get(
    "/oracle/redact/functions/actions", response_model=List[s.ActionOut],
)
def get_actions() -> List[s.ActionOut]:
    return Oracle.actions()

