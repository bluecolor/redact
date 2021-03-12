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
