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


@router.delete(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{id}", tags=["PlanInstances"],
    response_model=schemas.PlanInstanceOut
)
def delete(conn_id: int, plan_id: int, id: int, db: Session = Depends(get_db)):
    plan_instance: models.PlanInstance = (
        db.query(models.PlanInstance).filter(
            models.Connection.id == conn_id,
            models.Plan.id == plan_id,
            models.PlanInstance.id == id
        ).one()
    )
    pi = schemas.PlanInstanceOut.from_orm(plan_instance)
    db.delete(plan_instance)
    db.commit()
    return pi


@router.put(
    "/connections/{conn_id}/discovery/plans/{plan_id}/instances/{id}/stop", tags=["PlanInstances"],
    response_model=schemas.PlanInstanceOut
)
def stop(conn_id: int, plan_id: int, id: int, db: Session = Depends(get_db)):
    plan_instance = db.query(models.PlanInstance).filter(
        models.Plan.id == plan_id,
        models.Connection.id == conn_id,
        models.PlanInstance.id == id
    ).one()
    if plan_instance is None:
        return None

    if plan_instance.job_id is not None:
        ...

    plan_instance.status = 'stopped'
    db.add(plan_instance)
    db.commit()
    db.refresh(plan_instance)
    return schemas.PlanInstanceOut.from_orm(plan_instance)