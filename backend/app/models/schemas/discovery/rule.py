from typing import List, Optional, Any

from .base import Base
from .base import Rule, Plan, Connection


class RuleOut(Rule):
    plans: Optional[List[Plan]]


class RuleCreateIn(Base):
    name: str
    type: str
    severity: Optional[str]
    expression: str
    description: Optional[str]


class RuleUpdateIn(Base):
    name: str
    type: str
    severity: Optional[str]
    expression: str
    description: Optional[str]


class RuleDeleteOut(Base):
    name: str
