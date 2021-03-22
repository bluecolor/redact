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

from .base import Base


class Setting(Base):
    __tablename__ = "settings"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255), unique=True)
    value = Column(Text, nullable=True)
    description = Column(Text, nullable=True)

    def __init__(self, **kw):
        super().__init__(**kw)
