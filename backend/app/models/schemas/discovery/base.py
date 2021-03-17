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
    worker_count: Optional[int]
    sample_size: Optional[int]


class Rule(Base):
    name: str
    type: str
    severity: Optional[str]
    expression: str
    description: Optional[str]


class PlanInstanceOut(Base):
    plan: Plan
    status: Optional[str]
    worker_count: Optional[int]
    sample_size: Optional[int]


class Discovery(BaseModel):
    schema_name: str
    table_name: str
    column_name: Optional[str]
    rule: Rule
