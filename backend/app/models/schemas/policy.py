from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import column_property


class PolicyExpression(BaseModel):
    policy_expression_name: str
    expression: str
    policy_expression_description: Optional[str]


