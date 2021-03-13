from typing import Optional
from pydantic import BaseModel

from .base import Base


class Connection(Base):
    name: str
    username: str
    host: str
    port: int
    service: str


class ConnectionCreateIn(BaseModel):
    name: str
    username: str
    password: str
    host: str
    port: int
    service: str


class ConnectionUpdateIn(BaseModel):
    name: Optional[str]
    host: Optional[str]
    port: Optional[int]
    service: Optional[str]
    username: Optional[str]
    password: Optional[str]


class ConnectionTestIn(BaseModel):
    name: Optional[str]
    host: str
    port: int
    service: str
    username: str
    password: str
