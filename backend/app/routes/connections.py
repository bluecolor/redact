from typing import List, Any
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas as schemas
from app.vendors.base import Vendor
from .base import router
from app.database import get_db
from .base import get_current_active_user


@router.post(
    "/connections", tags=["Connections"], response_model=schemas.Connection
)
def create(request: schemas.ConnectionCreateIn, db: Session = Depends(get_db)):
    new_conn: models.Connection = models.Connection(**request.dict())
    db.add(new_conn)
    db.commit()
    db.refresh(new_conn)
    return schemas.Connection.from_orm(new_conn)


@router.get("/connections", response_model=List[schemas.Connection])
def index(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user),
):
    return db.query(models.Connection).all()


@router.get("/connections/{id}", response_model=schemas.Connection)
def show(id: int, db: Session = Depends(get_db)):
    return schemas.Connection.from_orm(
        db.query(models.Connection).filter(models.Connection.id == id).first()
    )


@router.put("/connections/{id}", response_model=schemas.Connection)
def update(
    connection: schemas.ConnectionUpdateIn,
    id: int,
    db: Session = Depends(get_db),
):
    # # get the existing data
    conn = db.query(models.Connection).get(id)
    if conn is None:
        return None

    for var, value in vars(connection).items():
        setattr(conn, var, value) if value else None

    db.add(conn)
    db.commit()
    db.refresh(conn)
    return schemas.Connection.from_orm(conn)


@router.delete("/connections/{id}", response_model=schemas.Connection)
def destroy(id: int, db: Session = Depends(get_db)):
    conn = db.query(models.Connection).filter(models.Connection.id == id).one()
    db.delete(conn)
    db.commit()
    return schemas.Connection.from_orm(conn)


@router.get("/connections/{id}/test", response_model=bool)
def test_with_id(id: int, db: Session = Depends(get_db)):
    conn = db.query(models.Connection).filter(models.Connection.id == id).one()
    vendor: Vendor = conn.get_vendor()
    try:
        return vendor.ping()
    except Exception as e:
        print(e)
        return False


@router.post("/connections/test", response_model=bool)
def test_with_payload(connection: schemas.ConnectionTestIn):
    conn: models.Connection = models.Connection(**connection.dict())
    vendor: Vendor = conn.get_vendor()
    return vendor.ping()


@router.get("/connections/{id}/users", response_model=List[Any])
def get_users(id: int, db: Session = Depends(get_db)):

    conn = db.query(models.Connection).get(id)
    vendor: Vendor = conn.get_vendor()
    # print(vendor.get_users())
    return vendor.get_users()
    # return []


@router.post("/connections/schemas", response_model=List[schemas.Schema])
def get_schemas_with_payload(connection: schemas.ConnectionTestIn):
    conn: models.Connection = models.Connection(**connection.dict())
    return md.get_schemas(conn)


@router.post("/connections/{id}/schemas", response_model=List[schemas.Schema])
def get_schemas(id: int, db: Session = Depends(get_db)):
    connection = db.query(models.Connection).get(id)
    return md.get_schemas(connection)

