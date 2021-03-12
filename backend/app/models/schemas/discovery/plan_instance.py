from typing import List, Optional, Any
from .base import Base, Plan, Rule


class PlanInstanceOut(Base):
    plan: Plan
    status: Optional[str]
    worker_count: Optional[int]
    sample_size: Optional[int]
