from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.mssql as s
from .base import router
from app.database import get_db
from app.vendors.mssql import SqlServer


@router.get(
    "/connections/{conn_id}/mssql/masks/columns",
    response_model=List[s.MaskedColumn],
)
def get_masked_columns(
    conn_id: int,
    schema_name: Optional[str] = None,
    table_name: Optional[str] = None,
    column_name: Optional[str] = None,
    db: Session = Depends(get_db),
) -> List[s.MaskedColumn]:
    conn = db.query(models.Connection).get(conn_id)
    mssql: SqlServer = conn.get_vendor()
    return mssql.get_masked_columns(schema_name, table_name, column_name)


@router.delete(
    "/connections/{conn_id}/mssql/masks/columns", response_model=bool,
)
def drop_mask(
    conn_id: int,
    schema_name: str,
    table_name: str,
    column_name: str,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    mssql: SqlServer = conn.get_vendor()
    mssql.drop_mask(schema_name, table_name, column_name)
    return True


@router.post(
    "/connections/{conn_id}/mssql/masks/columns/grant-unmask",
    response_model=bool,
)
def grant_unmask(
    conn_id: int, unmask: s.UnmaskIn, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    mssql: SqlServer = conn.get_vendor()
    mssql.grant_unmask(unmask.username)
    return True


@router.post(
    "/connections/{conn_id}/mssql/masks/columns/revoke-unmask",
    response_model=bool,
)
def revoke_unmask(
    conn_id: int, unmask: s.UnmaskIn, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    mssql: SqlServer = conn.get_vendor()
    mssql.revoke_unmask(unmask.username)
    return True


@router.post(
    "/connections/{conn_id}/mssql/masks/columns", response_model=bool,
)
def add_mask(
    conn_id: int, mask: s.MaskIn, db: Session = Depends(get_db),
) -> bool:
    conn = db.query(models.Connection).get(conn_id)
    mssql: SqlServer = conn.get_vendor()
    mssql.add_mask(mask)
    return True


@router.get(
    "/mssql/masks/functions", response_model=List[s.MaskingFunction],
)
def get_masking_functions() -> List[s.MaskedColumn]:
    return SqlServer.masking_functions()
