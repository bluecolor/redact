from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.oracle.redact as s
import app.models.schemas.metadata as ms
from .base import router
from app.database import get_db
from app.vendors.oracle import Oracle


@router.get(
    "/connections/{conn_id}/oracle/redact/columns",
    response_model=List[s.ColumnOut],
)
def get_all(
    conn_id: int,
    object_owner: Optional[str] = None,
    object_name: Optional[str] = None,
    db: Session = Depends(get_db),
) -> List[s.ColumnOut]:
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    return oracle.get_redaction_columns(object_owner, object_name)
