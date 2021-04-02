import json
from typing import List
from datetime import datetime
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

from .base import Base


class PlanInstance(Base):
    __tablename__ = "plan_instances"
    __table_args__ = {"extend_existing": True}

    sample_size = Column(Integer, default=5000)
    worker_count = Column(Integer, default=1)

    plan_id = Column(Integer, ForeignKey("plans.id"))
    plan = relationship("Plan", back_populates="plan_instances")

    schemas = Column(Text)
    discoveries = relationship("Discovery", back_populates="plan_instance")

    task_id = Column(String(255))

    status = Column(String(50))
    results = Column(Text)

    started_on = Column(
        DateTime, default=datetime.utcnow, server_default=func.now()
    )
    ended_on = Column(DateTime, nullable=True)

    @property
    def schema_list(self) -> List[str]:
        return json.loads(self.schemas)

    def __init__(self, **kw):
        super().__init__(**kw)

