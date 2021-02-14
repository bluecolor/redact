from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
from app.models.orm.connection import Connection
import app.models.schemas as schemas
from .base import router
from app.database import get_db
from app.oracle import ping


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
def index(db: Session = Depends(get_db)):
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
    connection = (
        db.query(models.Connection).filter(models.Connection.id == id).first()
    )
    db.delete(connection)
    db.commit()
    return schemas.Connection.from_orm(connection)


@router.get("/connections/{id}/test", response_model=bool)
def test(id: int, db: Session = Depends(get_db)):
    connection = (
        db.query(models.Connection).filter(models.Connection.id == id).first()
    )
    return ping(connection)

