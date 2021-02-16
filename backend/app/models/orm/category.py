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

from .base import Base
from app.models import schemas

class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255), unique=True)
    description = Column(String(255))
    policy_expression_name = Column(String(4000))
    function_type = Column(Integer)
    function_parameters = Column(String(4000))

    policy_expression: schemas.PolicyExpression

    def __init__(self, **kw):
        super().__init__(**kw)

    # created_by_id = Column(Integer, ForeignKey("users.id"))
    connection_id = Column(Integer, ForeignKey("connections.id"))
    connection= relationship("Connection", back_populates="categories")

