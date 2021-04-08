from typing import Optional, List
from pydantic import BaseModel
from .base import Base


class SettingIn(BaseModel):
    name: str
    value: str
    description: Optional[str]


class SettingOut(Base):
    name: Optional[str]
    value: Optional[str]
    description: Optional[str]

