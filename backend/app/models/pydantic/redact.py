from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import column_property


class PolicyIn(BaseModel):
    object_schema: str
    object_name: str
    column_name: str
    policy_name: str
    function_type: int
    expression: str


class DropPolicyIn(BaseModel):
    object_schema: str
    object_name: str
    policy_name: str


class AlterPolicyIn(BaseModel):
    object_schema: str
    object_name: str
    policy_name: str
    action: int
    column_name: str
    function_type: Optional[int]
    function_parameters: Optional[str]


class Policy(BaseModel):
    object_schema: str
    object_name: str
    column_name: str
    policy_name: str
    function_type: int
    expression: str


class CreatePolicyExpressionIn(BaseModel):
    policy_expression_name: str
    expression: str
    policy_expression_description: Optional[str]


class ApplyPolicyExprToColIn(BaseModel):
    object_schema: str
    object_name: str
    column_name: str
    policy_expression_name: str


class UpdatePolicyExpressionIn(BaseModel):
    policy_expression_name: str
    expression: str
