from typing import List, Optional, Any
from app.models.orm import plan_instance

from app.models.schemas import connection
from .base import Base
from .rule import Rule
from .base import Plan


class PlanOut(Plan):
    rules: Optional[List[Rule]]


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
