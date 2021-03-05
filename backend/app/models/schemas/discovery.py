from typing import List, Optional, Any
from .base import Base
from sqlalchemy.orm import column_property
from . import Connection

class PlanOut(Base):
    name: str

class RuleOut(Base):
    name: str
    schemas: Optional[str]
    type: str
    severity: Optional[str]
    expression: str
    plans: Optional[List[PlanOut]]

class RuleCreateIn(Base):
    name: str
    schemas: Optional[str]
    type: str
    severity: Optional[str]
    expression: str
