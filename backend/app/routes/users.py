from fastapi import Depends
from typing import List
from sqlalchemy.orm import Session
import app.models.orm as model
from app.models.schemas import User, UserCreateIn, UserOut, UserUpdateIn
from .base import router
from app.database import get_db
import app.models.orm as models
import app.models.schemas as schemas
from pydantic import parse_obj_as


@router.post("/users", tags=["Users"], response_model=UserOut)
async def create_user(request: UserCreateIn, db: Session = Depends(get_db)):
    new_user: models.User = models.User(**request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return schemas.UserOut.from_orm(new_user)


@router.get("/users", tags=["Users"], response_model=List[UserOut])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return parse_obj_as(List[UserOut], users)


@router.put("/users/{id}", response_model=schemas.UserOut)
def update(
    user_in: schemas.UserUpdateIn,
    id: int,
    db: Session = Depends(get_db),
):
    # # get the existing data
    user = db.query(models.User).get(id)
    if user is None:
        return None

    for var, value in vars(user_in).items():
        setattr(user, var, value) if value else None

    db.add(user)
    db.commit()
    db.refresh(user)
    return schemas.UserOut.from_orm(user)


@router.delete("/users/{id}", response_model=schemas.UserOut)
def destroy(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).get(id)
    db.delete(user)
    db.commit()
    return schemas.UserOut.from_orm(user)


@router.get("/users/{id}", response_model=schemas.UserOut)
def show(id: int, db: Session = Depends(get_db)):
    return schemas.UserOut.from_orm(db.query(models.User).get(id))
