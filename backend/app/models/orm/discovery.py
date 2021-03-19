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


class Discovery(Base):
    __tablename__ = "discoveries"
    __table_args__ = {"extend_existing": True}

    schema_name = Column(String(128))
    table_name = Column(String(128))
    column_name = Column(String(128))

    plan_instance_id = Column(
        Integer, ForeignKey("plan_instances.id"), nullable=True
    )
    plan_instance = relationship("PlanInstance", back_populates="discoveries")

    rule_id = Column(Integer, ForeignKey("rules.id"))
    rule = relationship("Rule", back_populates="discoveries")

    def __init__(self, **kw):
        super().__init__(**kw)

