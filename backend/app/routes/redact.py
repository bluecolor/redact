from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
from app.models.orm.connection import Connection
import app.models.pydantic as schemas
from .base import router
from app.database import get_db
from app.oracle import redact


@router.post(
    "/connections/{conn_id}/redact/policies", response_model=bool,
)
def add_policy(
    policy: schemas.PolicyIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.add_policy(connection, policy.dict())
    return True
