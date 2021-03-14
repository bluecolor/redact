from typing import List, Optional, Any
from app.models.schemas import connection
from .base import Base, Rule


class DiscoveryOut(Base):
    schema_name: str
    table_name: str
    column_name: Optional[str]
    rule: Rule


class DiscoveryGroupByRuleOut(Base):
    rule: Rule
    count: int
