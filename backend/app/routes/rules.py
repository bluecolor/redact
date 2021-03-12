from sqlalchemy import func
from typing import List, Optional, Union
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func, mode
import app.models.orm as models
import app.models.schemas as schemas
from .base import router
from app.database import get_db
from app.settings.arq import settings as redis_settings
from arq.connections import ArqRedis, create_pool
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page, Params
from pydantic import parse_obj_as


@router.get(
    "/connections/{conn_id}/discovery/rules/{id}",
    response_model=schemas.RuleOut,
)
def get_one(
    conn_id: int, id: int, db: Session = Depends(get_db)
) -> schemas.RuleOut:
    rule = (
        db.query(models.Rule)
        .outerjoin(models.Connection)
        .filter(models.Connection.id == conn_id, models.Rule.id == id)
        .one()
    )
    return schemas.RuleOut.from_orm(rule)


@router.get(
    "/connections/{conn_id}/discovery/rules",
    response_model=List[schemas.RuleOut],
)
def get_all(
    conn_id: int, db: Session = Depends(get_db)
) -> List[schemas.RuleOut]:
    rules = (
        db.query(models.Rule)
        .filter(models.Rule.connection_id == conn_id)
        .all()
    )
    return parse_obj_as(List[schemas.RuleOut], rules)


@router.post(
    "/connections/{conn_id}/discovery/rules",
    tags=["Rules"],
    response_model=schemas.RuleOut,
)
def create(
    conn_id: int, rule: schemas.RuleCreateIn, db: Session = Depends(get_db)
):
    new_rule: models.Rule = models.Rule(
        **{**rule.dict(), "connection_id": conn_id}
    )
    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)

    return schemas.RuleOut.from_orm(new_rule)


@router.put(
    "/connections/{conn_id}/discovery/rules/{id}",
    response_model=schemas.RuleOut,
)
def update(
    rule: schemas.RuleUpdateIn,
    conn_id: int,
    id: int,
    db: Session = Depends(get_db),
):
    rule = (
        db.query(models.Rule)
        .filter(models.Connection.id == conn_id, models.Rule.id == id)
        .one()
    )

    if rule is None:
        return None

    for var, value in vars(rule).items():
        setattr(rule, var, value) if value else None

    db.add(rule)
    db.commit()
    db.refresh(rule)
    return schemas.RuleOut.from_orm(rule)


@router.delete(
    "/connections/{conn_id}/discovery/rules/{id}",
    response_model=schemas.RuleDeleteOut,
)
def delete(conn_id: int, id: int, db: Session = Depends(get_db)):
    rule = db.query(models.Rule).get(id)
    db.delete(rule)
    db.commit()
    return schemas.RuleDeleteOut.from_orm(rule)
