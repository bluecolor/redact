from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import column_property


class ExpressionOut(BaseModel):
    policy_expression_name: str
    expression: str
    object_owner: Optional[str]
    object_name: Optional[str]
    column_name: Optional[str]
    policy_expression_description: Optional[str]


class ExpressionUpdateIn(BaseModel):
    policy_expression_name: str
    expression: str


class ExpressionApplyIn(BaseModel):
    object_schema: str
    object_name: str
    column_name: str
    policy_expression_name: str


class ExpressionCreateIn(BaseModel):
    policy_expression_name: str
    expression: str
    policy_expression_description: Optional[str]
