from pydantic import BaseModel


class Table(BaseModel):
    owner: str
    table_name: str

