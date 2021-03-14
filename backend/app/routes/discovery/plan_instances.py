from sqlalchemy import func
from typing import List, Optional, Union
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func, mode
import app.models.orm as models
import app.models.schemas.discovery as s
from .base import router
from app.database import get_db
from app.settings.arq import settings as redis_settings
from arq.connections import ArqRedis, create_pool
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page, Params
from pydantic import parse_obj_as


@router.delete(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{id}",
    tags=["PlanInstances"],
    response_model=s.PlanInstanceOut,
)
def delete(conn_id: int, plan_id: int, id: int, db: Session = Depends(get_db)):
    plan_instance: models.PlanInstance = (
        db.query(models.PlanInstance)
        .filter(
            models.Connection.id == conn_id,
            models.Plan.id == plan_id,
            models.PlanInstance.id == id,
        )
        .one()
    )
    pi = s.PlanInstanceOut.from_orm(plan_instance)
    db.delete(plan_instance)
    db.commit()
    return pi


@router.get(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{id}",
    tags=["PlanInstances"],
    response_model=s.PlanInstanceOut,
)
def get_one(
    conn_id: int, plan_id: int, id: int, db: Session = Depends(get_db)
):
    plan_instance: models.PlanInstance = (
        db.query(models.PlanInstance)
        .filter(
            models.Connection.id == conn_id,
            models.Plan.id == plan_id,
            models.PlanInstance.id == id,
        )
        .one()
    )
    return s.PlanInstanceOut.from_orm(plan_instance)


@router.put(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{id}/stop",
    tags=["PlanInstances"],
    response_model=s.PlanInstanceOut,
)
def stop(conn_id: int, plan_id: int, id: int, db: Session = Depends(get_db)):
    plan_instance = (
        db.query(models.PlanInstance)
        .filter(
            models.Plan.id == plan_id,
            models.Connection.id == conn_id,
            models.PlanInstance.id == id,
        )
        .one()
    )
    if plan_instance is None:
        return None

    if plan_instance.job_id is not None:
        ...

    plan_instance.status = "stopped"
    db.add(plan_instance)
    db.commit()
    db.refresh(plan_instance)
    return s.PlanInstanceOut.from_orm(plan_instance)


@router.get(
    "/connections/{conn_id}/discovery/plans/instances",
    tags=["PlanInstances"],
    response_model=List[s.PlanInstanceOut],
)
async def get_all(conn_id: int, db: Session = Depends(get_db)):
    plan_instances = (
        db.query(models.PlanInstance)
        .outerjoin(models.Plan)
        .filter(models.Plan.connection_id == conn_id)
        .all()
    )
    return parse_obj_as(List[s.PlanInstanceOut], plan_instances)


@router.get(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances",
    tags=["PlanInstances"],
    response_model=List[s.PlanInstanceOut],
)
async def get_by_plan(
    conn_id: int, plan_id: int, db: Session = Depends(get_db)
):
    plan_instances = (
        db.query(models.PlanInstance)
        .filter(
            models.Plan.connection_id == conn_id,
            models.PlanInstance.plan_id == plan_id,
        )
        .all()
    )
    return parse_obj_as(List[s.PlanInstanceOut], plan_instances)

