from typing import Optional
from pydantic import BaseModel
from sqlalchemy.sql.expression import column


class Table(BaseModel):
    owner: str
    table_name: str


class DataStore(Table):
    type: Optional[str]


class Column(Table):
    column_name: str
    data_type: str


class ColumnIn(Table):
    column_name: str


class ColumnInOut(Table):
    column_name: str


class ObjectOwner(BaseModel):
    name: str
