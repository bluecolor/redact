from typing import List, Optional, Any
from app.models.orm import plan_instance

from app.models.schemas import connection
from .base import Base
from .rule import Rule
from .base import Plan
from app.settings import SAMPLE_SIZE, WORKER_COUNT


class PlanOut(Plan):
    rules: Optional[List[Rule]]


class PlanCreateIn(Base):
    name: str
    schemas: str
    rules: List[int]
    worker_count: Optional[int] = SAMPLE_SIZE
    sample_size: Optional[int] = WORKER_COUNT
    description: Optional[str]


class PlanUpdateIn(Base):
    name: str
    schemas: str
    rules: List[int]
    worker_count: Optional[int]
    sample_size: Optional[int]
    description: Optional[str]


class PlanDeleteOut(Base):
    name: str
