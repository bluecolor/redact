from typing import Optional, List
from pydantic import BaseModel


class ExportIn(BaseModel):
    options: List[str]
