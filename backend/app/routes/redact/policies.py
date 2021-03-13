from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.redact as s
from .base import router
from app.database import get_db
from app.oracle import redact


@router.post(
    "/connections/{conn_id}/redact/policies", response_model=bool,
)
def create(
    policy: s.PolicyCreateIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.add_policy(connection, policy.dict())
    return True


@router.get(
    "/connections/{conn_id}/redact/policies", response_model=List[s.PolicyOut],
)
def get_all(
    conn_id: int,
    owner: Optional[str] = None,
    table_name: Optional[str] = None,
    db: Session = Depends(get_db),
) -> List[s.PolicyOut]:
    connection = db.query(models.Connection).get(conn_id)
    return redact.get_policies(connection, owner=owner, table_name=table_name)


@router.put(
    "/connections/{conn_id}/redact/policies/delete", response_model=bool,
)
def delete(
    policy: s.PolicyDeleteIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.drop_policy(connection, policy.dict())
    return True


@router.put(
    "/connections/{conn_id}/redact/policies", response_model=bool,
)
def update(
    policy: s.PolicyUpdateIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.alter_policy(connection, policy.dict())
    return True

