from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.oracle.redact as s
import app.models.schemas.metadata as ms
from .base import router
from app.database import get_db


@router.get(
    "/connections/oracle/{conn_id}/redact/columns",
    response_model=List[s.ColumnOut],
)
def get_all(
    conn_id: int,
    object_owner: Optional[str] = None,
    object_name: Optional[str] = None,
    db: Session = Depends(get_db),
) -> List[s.ColumnOut]:
    connection = db.query(models.Connection).get(conn_id)
    return redact.get_columns(connection, object_owner, object_name)
