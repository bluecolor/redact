from typing import Optional
from pydantic import BaseModel

from .base import Base


class CategoryCreateIn(BaseModel):
    name: str
    description: Optional[str]
    options: str


class CategoryUpdateIn(BaseModel):
    name: str
    description: Optional[str]
    options: Optional[str]


class CategoryOut(Base):
    id: int
    name: str
    description: Optional[str]
    options: Optional[str]
