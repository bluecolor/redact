from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import column_property
from app.models.schemas import PolicyExpression

from .base import Base

class CategoryCreateIn(BaseModel):
    name: str
    description: Optional[str]
    function_type: int
    function_parameters: Optional[str]
    policy_expression_name: str

class CategoryOut(Base):
    id: str
    name: str
    description: Optional[str]
    function_type: int
    function_parameters: Optional[str]
    policy_expression: Optional[PolicyExpression]
