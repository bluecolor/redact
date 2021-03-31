from typing import List, Optional, Any
from app.models.schemas import Table
from .base import Base, Rule, BaseModel, Discovery


class DiscoveryOut(Base):
    schema_name: str
    table_name: str
    column_name: Optional[str]
    rule: Rule


class DiscoveryGroupByRuleOut(Base):
    rule: Rule
    count: int


class DiscoveryGroupBySchemaOut(BaseModel):
    schema_name: str
    count: int


class SearchResult(BaseModel):
    hit: bool
    table: Optional[Table]
    discovery: Optional[Discovery]
