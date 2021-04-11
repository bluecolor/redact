from typing import Optional
from app.models.schemas.metadata import Column
from pydantic import BaseModel


class MaskedColumn(Column):
    masking_function: str


class MaskingFunction(BaseModel):
    title: str
    name: str
    args: Optional[str]


class MaskIn(BaseModel):
    schema_name: str
    table_name: str
    column_name: str
    func: str
    args: Optional[str]
