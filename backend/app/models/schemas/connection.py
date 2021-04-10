from typing import Optional
from pydantic import BaseModel

from .base import Base


class Connection(Base):
    name: str
    vendor: str
    username: str
    host: str
    port: int
    database: str
    options: Optional[str]


class ConnectionCreateIn(BaseModel):
    name: str
    vendor: str
    username: str
    password: str
    host: str
    port: int
    database: str
    options: Optional[str]


class ConnectionUpdateIn(BaseModel):
    name: Optional[str]
    vendor: Optional[str]
    host: Optional[str]
    port: Optional[int]
    database: Optional[str]
    username: Optional[str]
    password: Optional[str]
    options: Optional[str]


class ConnectionTestIn(BaseModel):
    name: Optional[str]
    vendor: Optional[str]
    host: str
    port: int
    database: str
    username: str
    password: str
