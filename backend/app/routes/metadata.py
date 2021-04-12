from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
from app.models.orm.connection import Connection
import app.models.schemas as schemas
from app.routes.base import router
from app.database import get_db
from app.vendors.base import Vendor


@router.get(
    "/connections/{conn_id}/metadata/schemas",
    response_model=List[schemas.Schema],
)
def get_schemas(conn_id: int, db: Session = Depends(get_db)):
    conn = db.query(models.Connection).get(conn_id)
    vendor: Vendor = conn.get_vendor()
    return vendor.get_schemas()


@router.get(
    "/connections/{conn_id}/metadata/tables",
    response_model=List[schemas.Table],
)
def get_tables(
    conn_id: int, schema_name: Optional[str], db: Session = Depends(get_db)
):
    conn = db.query(models.Connection).get(conn_id)
    vendor: Vendor = conn.get_vendor()
    return vendor.get_tables(schema_name)


@router.get(
    "/connections/{conn_id}/metadata/columns",
    response_model=List[schemas.Column],
)
def get_columns(
    conn_id: int,
    schema_name: Optional[str] = None,
    table_name: Optional[str] = None,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    vendor: Vendor = conn.get_vendor()
    return vendor.get_columns(schema_name, table_name)


@router.get(
    "/connections/{conn_id}/metadata/search",
    response_model=List[schemas.MetadataOut],
)
def search(
    conn_id: int, q: str, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    vendor: Vendor = conn.get_vendor()
    return vendor.search(q)[0:10]


@router.get(
    "/connections/{conn_id}/metadata/columns/sample",
    response_model=List[dict],
)
def get_col_sample_data(
    conn_id: int,
    schema_name: str,
    table_name: str,
    column_name: str,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    vendor: Vendor = conn.get_vendor()
    return vendor.get_sample(schema_name, table_name, column_name)

