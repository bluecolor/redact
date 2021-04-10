from typing import Optional
from pydantic import BaseModel


class Schema(BaseModel):
    schema_name: str


class Table(Schema):
    table_name: str


class Column(Table):
    column_name: str
    data_type: Optional[str]


class ColumnIn(Table):
    column_name: str


class MetadataOut(BaseModel):
    type: str
    schema_name: str
    table_name: str
    column_name: Optional[str]
