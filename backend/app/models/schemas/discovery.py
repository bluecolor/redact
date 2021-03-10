from typing import List, Optional, Any
from app.models.orm import plan_instance

from app.models.schemas import connection
from .base import Base
from sqlalchemy.orm import column_property
from . import Connection

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

class RuleDeleteOut(Base):
    name: str


class PlanCreateIn(Base):
    name: str
    schemas: str
    rules: List[int]
    description: Optional[str]

class PlanDeleteOut(Base):
    name: str

class PlanInstanceOut(Base):
    plan: PlanOut
    status: Optional[str]
    worker_count: Optional[int]
    sample_size: Optional[int]


class DiscoveryOut(Base):
    schema_name: str
    table_name: str
    column_name: Optional[str]
    rule: Rule

class DiscoveryByRuleOut(Base):
    rule_id: int
    count: int
