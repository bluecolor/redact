import signal
from sqlalchemy import func
from typing import List, Optional, Union
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func, mode
import app.models.orm as models
import app.models.schemas.discovery as s
from .base import router
from app.database import get_db
from arq.connections import ArqRedis, create_pool
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page, Params
from pydantic import parse_obj_as
from app.celery import celery_app


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
        .outerjoin(models.Plan)
        .outerjoin(models.Connection)
        .filter(
            models.Plan.id == plan_id,
            models.Connection.id == conn_id,
            models.PlanInstance.id == id,
        )
        .one()
    )
    if plan_instance is None:
        return None

    if plan_instance.task_id is not None:
        celery_app.control.revoke(
            plan_instance.task_id, terminate=True, signal=signal.SIGKILL
        )

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
async def get_all(
    conn_id: int,
    plan_id: Optional[int] = None,
    created_on: Optional[str] = None,  # todo
    status: Optional[str] = None,
    db: Session = Depends(get_db),
):

    filters: List = [models.Plan.connection_id == conn_id]
    if plan_id:
        filters.append(models.PlanInstance.plan_id == plan_id)
    if status:
        filters.append(models.PlanInstance.status == status)

    plan_instances = (
        db.query(models.PlanInstance)
        .outerjoin(models.Plan)
        .filter(*filters)
        .order_by(models.PlanInstance.created_on.desc())
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
        .order_by(models.PlanInstance.created_on.desc())
        .all()
    )
    return parse_obj_as(List[s.PlanInstanceOut], plan_instances)

