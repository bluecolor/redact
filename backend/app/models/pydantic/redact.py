from typing import Optional
from pydantic import BaseModel


class PolicyIn(BaseModel):
    object_schema: str
    object_name: str
    column_name: str
    policy_name: str
    function_type: int
    expression: str


class Policy(BaseModel):
    object_schema: str
    object_name: str
    column_name: str
    policy_name: str
    function_type: int
    expression: str
