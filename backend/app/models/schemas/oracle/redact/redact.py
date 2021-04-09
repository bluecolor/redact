from typing import Optional

from sqlalchemy.sql import expression
from app.models.schemas.base import Base, BaseModel
from app.models.schemas.metadata import ColumnIn
from .base import ColumnOut, Expression


class ColumnAnswerOut(BaseModel):
    owner: str
    table_name: str
    column_name: str
    column: Optional[ColumnOut]
    expression: Optional[Expression]
