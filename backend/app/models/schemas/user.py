from typing import Optional

from pydantic import BaseModel, EmailStr

from .base import Base


class User(Base):
    name: str
    email: Optional[EmailStr]
    username: str


class UserOut(Base):
    name: str
    email: Optional[EmailStr]
    username: str
    api_key: Optional[str]
    preferences: Optional[str]


class UserCreateIn(BaseModel):
    name: str
    email: EmailStr
    username: str


class UserUpdateIn(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    username: Optional[str]


class PreferencesIn(BaseModel):
    preferences: str
