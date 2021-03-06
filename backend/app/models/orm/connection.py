from cryptography.fernet import Fernet

from sqlalchemy.orm import relationship
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
from app.settings import FERNET_KEY

fernet = Fernet(str.encode(FERNET_KEY))


class Connection(Base):
    __tablename__ = "connections"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255), unique=True)
    host = Column(String(255))
    port = Column(Integer)
    service = Column(String(100))
    username = Column(String(255))
    encrypted_password = Column(String)

    categories = relationship("Category", back_populates="connection")
    plans = relationship("Plan", back_populates="connection")
    rules = relationship("Rule", back_populates="connection")


    def __init__(self, **kw):
        super().__init__(**kw)

    @property
    def password(self):
        return self.encrypted_password

    @property
    def password_plain(self):
        return fernet.decrypt(self.encrypted_password).decode()

    @password.setter
    def password(self, password):
        self.encrypted_password = fernet.encrypt(str.encode(password))

    @property
    def dsn(self):
        port = f":{self.port}" if self.port else ""
        return f"{self.host}{port}/{self.service}"

    def verify_password(self, password):
        return (
            self.encrypted_password
            and fernet.encrypt(str.encode(password)) == self.encrypted_password
        )

