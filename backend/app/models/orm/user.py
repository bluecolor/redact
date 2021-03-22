from sqlalchemy import (
    func,
    BigInteger,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
)
from passlib.apps import custom_app_context as pwd_context

from .base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255))
    email = Column(String(255))
    username = Column(String(255))
    password_hash = Column(String)

    disabled = Column(Boolean, default=False)

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

