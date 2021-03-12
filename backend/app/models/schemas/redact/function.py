from typing import Optional
from .base import BaseModel


class FunctionTypeOut(BaseModel):
    function_type: int
    name: str
    description: Optional[str]


class FunctionParametersOut(BaseModel):
    function_parameters: str


class ActionOut(BaseModel):
    action: int
    name: str
    description: Optional[str]
