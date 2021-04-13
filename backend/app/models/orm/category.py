from typing import Text
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
from sqlalchemy.orm.base import attribute_str

from .base import Base
from app.models.schemas.oracle.redact.base import Expression
from app.vendors.oracle import Oracle


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255), unique=True)
    description = Column(String(255))

    options = Column(Text)

    # policy_expression_name = Column(String(4000))
    # function_type = Column(Integer)
    # function_parameters = Column(String(4000))

    # policy_expression: Expression

    # @property
    # def function_type_name(self):
    #     for ft in Oracle.function_types:
    #         if ft.function_type == self.function_type:
    #             return ft.name

    def __init__(self, **kw):
        super().__init__(**kw)

    # created_by_id = Column(Integer, ForeignKey("users.id"))
    connection_id = Column(Integer, ForeignKey("connections.id"))
    connection = relationship("Connection", back_populates="categories")

