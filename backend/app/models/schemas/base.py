from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel):
    id: Optional[int]
    created_on: Optional[datetime]
    updated_on: Optional[datetime]

    class Config:
        orm_mode = True
