from typing import Optional
from pydantic import BaseModel


class TokenOut(BaseModel):
    access_token: str
    token_type: Optional[str] = "bearer"
