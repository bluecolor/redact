from typing import List, Optional, Any

from app.models.schemas import connection
from .base import Base
from sqlalchemy.orm import column_property
from . import Connection

class Plan(Base):
    name: str
    connection_id: Optional[int]
    connection: Optional[Connection]
    schemas: str
    description: Optional[str]

class Rule(Base):
    name: str
    type: str
    severity: Optional[str]
    expression: str
    description: Optional[str]
    connection_id: int
    connection: Optional[Connection]


class PlanOut(Plan):
    rules: Optional[List[Rule]]

class RuleOut(Rule):
    plans: Optional[List[Plan]]


class RuleCreateIn(Base):
    name: str
    type: str
    severity: Optional[str]
    expression: str
    description: Optional[str]


class PlanCreateIn(Base):
    name: str
    schemas: str
    rules: List[int]
    description: Optional[str]