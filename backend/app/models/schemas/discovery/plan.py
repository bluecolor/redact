from typing import List, Optional, Any
from app.models.orm import plan_instance

from app.models.schemas import connection
from .base import Base
from . import Connection
from .rule import Rule
from .base import Plan


class PlanOut(Plan):
    rules: Optional[List[Rule]]


class RuleUpdateIn(Base):
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


class PlanUpdateIn(Base):
    name: str
    schemas: str
    rules: List[int]
    description: Optional[str]


class PlanDeleteOut(Base):
    name: str
