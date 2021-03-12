from typing import Optional
from datetime import datetime
from app.models.schemas.base import Base, BaseModel


class Connection(Base):
    name: str
    username: str
    host: str
    port: int
    service: str


class Plan(Base):
    name: str
    connection_id: Optional[int]
    connection: Optional[Connection]
    schemas: str
    status: Optional[str]
    description: Optional[str]


class Rule(Base):
    name: str
    type: str
    severity: Optional[str]
    expression: str
    description: Optional[str]
