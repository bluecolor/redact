from sqlalchemy import (
    func,
    BigInteger,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Text,
)
from passlib.apps import custom_app_context as pwd_context

from .base import Base
from app.utils import generate_token


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255))
    email = Column(String(255))
    username = Column(String(255))
    password_hash = Column(String)

    disabled = Column(Boolean, default=False)

    api_key = Column(
        String(40),
        default=lambda: generate_token(40),
        unique=True,
        nullable=True,
    )

    preferences = Column(Text, nullable=True)

    def __init__(self, **kw):
        super().__init__(**kw)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return self.password_hash and pwd_context.verify(
            password, self.password_hash
        )

    def regenerate_api_key(self):
        self.api_key = generate_token(40)

