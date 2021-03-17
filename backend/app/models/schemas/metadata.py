from typing import Optional
from pydantic import BaseModel


class Table(BaseModel):
    owner: str
    table_name: str


class DataStore(Table):
    type: Optional[str]


class Column(Table):
    column_name: str
    data_type: str


class ObjectOwner(BaseModel):
    name: str
