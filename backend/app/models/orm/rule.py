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

from .base import Base, plan_rules


class Rule(Base):
    __tablename__ = "rules"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255), unique=True)
    type = Column(String(50))
    severity = Column(String(100))
    expression = Column(Text)
    description = Column(Text, nullable=True)

    plans = relationship("Plan", secondary=plan_rules, back_populates="rules")
    discoveries = relationship("Discovery", back_populates="rule")

    connection_id = Column(Integer, ForeignKey("connections.id"))
    connection = relationship("Connection", back_populates="rules")

    def __init__(self, **kw):
        super().__init__(**kw)

