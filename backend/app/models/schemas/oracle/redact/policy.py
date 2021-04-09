from typing import Optional

from app.models.schemas.metadata import Table
from .base import BaseModel


class PolicyOut(BaseModel):
    object_owner: str
    object_name: str
    policy_name: str
    expression: str
    enable: str
    policy_description: Optional[str]


class PolicyCreateIn(BaseModel):
    object_schema: str
    object_name: str
    column_name: str
    policy_name: str
    function_type: int
    function_parameters: Optional[str]
    expression: str


class PolicyUpdateIn(BaseModel):
    object_schema: str
    object_name: str
    policy_name: str
    action: int
    column_name: Optional[str]
    expression: Optional[str]
    function_type: Optional[int]
    function_parameters: Optional[str]
    policy_description: Optional[str]


class PolicyEnableIn(BaseModel):
    object_schema: str
    object_name: str
    policy_name: str


class PolicyDisableIn(BaseModel):
    object_schema: str
    object_name: str
    policy_name: str


class PolicyTableAnswer(BaseModel):
    table: Table
    policy: Optional[PolicyOut]
