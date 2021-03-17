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
    Table,
)

from .base import Base, plan_rules
from .plan_instance import PlanInstance

# from app.settings.discovery import SAMPLE_SIZE, WORKER_COUNT


class Plan(Base):
    __tablename__ = "plans"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255), unique=True)
    rules = relationship("Rule", secondary=plan_rules, back_populates="plans")
    schemas = Column(Text)

    sample_size = Column(Integer, default=5000)
    worker_count = Column(Integer, default=4)

    description = Column(Text)

    connection_id = Column(Integer, ForeignKey("connections.id"))
    connection = relationship("Connection", back_populates="plans")

    plan_instances = relationship("PlanInstance", back_populates="plan")

    status = Column(String(50))

    def get_new_instance(self):
        return PlanInstance(
            plan_id=self.id,
            plan=self,
            schemas=self.schemas,
            sample_size=self.sample_size,
            worker_count=self.worker_count,
            status="ready",
        )

    def __init__(self, **kw):
        super().__init__(**kw)

