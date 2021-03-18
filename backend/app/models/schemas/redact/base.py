from typing import Optional
from datetime import datetime
from app.models.schemas.base import Base, BaseModel


class Expression(BaseModel):
    policy_expression_name: str
    expression: str
    policy_expression_description: Optional[str]


class Policy(BaseModel):
    object_schema: str
    object_name: str
    column_name: str
    policy_name: str
    function_type: int
    expression: str


class ColumnOut(BaseModel):
    object_owner: str
    object_name: str
    column_name: str
    function_type: str
    function_parameters: Optional[str]
    regexp_pattern: Optional[str]
    regexp_replace_string: Optional[str]
    regexp_position: Optional[int]
    regexp_occurance: Optional[int]
    regexp_match_parameter: Optional[str]
    column_description: Optional[str]
