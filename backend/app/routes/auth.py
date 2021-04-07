from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from typing import List
from sqlalchemy.orm import Session
import app.models.orm as model
from .base import router
from app.database import get_db
import app.models.orm as models
import app.models.schemas as schemas
from pydantic import parse_obj_as
from app.settings import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    SECRET_KEY,
    JWT_ALGORITHM,
)
from app.tasks import notify_login


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(model.User).filter(model.User.username == username).one()
    if not user:
        return False
    if not user.verify_password(password=password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, str(SECRET_KEY), algorithm=JWT_ALGORITHM
    )
    return encoded_jwt


@router.post("/auth/login", response_model=schemas.TokenOut)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    notify_login(user)
    return {"access_token": access_token, "token_type": "bearer"}
