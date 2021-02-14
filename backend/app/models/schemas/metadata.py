from pydantic import BaseModel


class Table(BaseModel):
    owner: str
    table_name: str


class Column(Table):
    column_name: str
    data_type: str
