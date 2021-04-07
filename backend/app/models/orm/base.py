from sqlalchemy import (
    func,
    BigInteger,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Table,
    PrimaryKeyConstraint,
)
from datetime import datetime

# from sqlalchemy_utils import generic_repr

from app.database import Base as DeclarativeBase


# @generic_repr
class Base(DeclarativeBase):
    __abstract__ = True
    created_on = Column(
        DateTime, default=datetime.utcnow, server_default=func.now()
    )
    updated_on = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        server_default=func.now(),
    )
    id = Column(Integer, primary_key=True, autoincrement=True)


plan_rules = Table(
    "plan_rules",
    Base.metadata,
    Column("plan_id", Integer, ForeignKey("plans.id")),
    Column("rule_id", Integer, ForeignKey("rules.id")),
    PrimaryKeyConstraint("plan_id", "rule_id"),
)

plan_instance_rules = Table(
    "plan_instance_rules",
    Base.metadata,
    Column("plan_instance_id", Integer, ForeignKey("plan_instances.id")),
    Column("rule_id", Integer, ForeignKey("rules.id")),
    PrimaryKeyConstraint("plan_instance_id", "rule_id"),
)
