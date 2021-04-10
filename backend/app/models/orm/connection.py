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
    Text,
)
from passlib.apps import custom_app_context as pwd_context

from .base import Base
from app.settings import FERNET_KEY
from app.vendors import vendors

fernet = Fernet(str.encode(FERNET_KEY))


class Connection(Base):
    __tablename__ = "connections"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255), unique=True, nullable=False)
    vendor = Column(String(50))
    host = Column(String(255))
    port = Column(Integer)
    database = Column(String(100))
    username = Column(String(255))
    encrypted_password = Column(String)
    options = Column(Text)

    categories = relationship("Category", back_populates="connection")
    plans = relationship("Plan", back_populates="connection")
    rules = relationship("Rule", back_populates="connection")

    def __init__(self, **kw):
        super().__init__(**kw)

    @property
    def password(self):
        return self.encrypted_password

    @property
    def password_plain(self) -> str:
        return fernet.decrypt(self.encrypted_password.encode()).decode()

    @password.setter
    def password(self, password):
        self.encrypted_password = fernet.encrypt(str.encode(password)).decode()

    @property
    def dsn(self):
        port = f":{self.port}" if self.port else ""
        return f"{self.host}{port}/{self.database}"

    def verify_password(self, password):
        return (
            self.encrypted_password
            and fernet.encrypt(str.encode(password)) == self.encrypted_password
        )

    def get_vendor(self):
        return vendors[self.vendor](self)

    def ping(self):
        return self.get_vendor().ping()
