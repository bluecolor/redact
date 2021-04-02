from sqlalchemy import func
from typing import List, Optional, Union
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func, mode
import app.models.orm as models
import app.models.schemas.discovery as s
from .base import router
from app.database import get_db
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page, Params
from pydantic import parse_obj_as
from app.tasks import start_plan


@router.get(
    "/connections/{conn_id}/discovery/plans", response_model=List[s.PlanOut],
)
def get_all(conn_id: int, db: Session = Depends(get_db)) -> List[s.PlanOut]:
    plans = (
        db.query(models.Plan)
        .filter(models.Plan.connection_id == conn_id)
        .all()
    )
    return parse_obj_as(List[s.PlanOut], plans)


@router.get(
    "/connections/{conn_id}/discovery/plans/{id}", response_model=s.PlanOut,
)
def get_one(
    conn_id: int, id: int, db: Session = Depends(get_db)
) -> List[s.PlanOut]:
    plan = (
        db.query(models.Plan)
        .filter(models.Plan.connection_id == conn_id, models.Plan.id == id)
        .one()
    )
    return s.PlanOut.from_orm(plan)


@router.post(
    "/connections/{conn_id}/discovery/plans",
    tags=["Plans"],
    response_model=s.PlanOut,
)
def create(conn_id: int, plan: s.PlanCreateIn, db: Session = Depends(get_db)):
    rules = db.query(models.Rule).filter(models.Rule.id.in_(plan.rules)).all()
    new_plan: models.Plan = models.Plan(
        **{**plan.dict(), "connection_id": conn_id, "rules": rules}
    )
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return s.PlanOut.from_orm(new_plan)


@router.put(
    "/connections/{conn_id}/discovery/plans/{id}", response_model=s.PlanOut,
)
async def update(
    new_plan: s.PlanUpdateIn,
    conn_id: int,
    id: int,
    db: Session = Depends(get_db),
):
    plan = (
        db.query(models.Plan)
        .filter(models.Connection.id == conn_id, models.Plan.id == id)
        .one()
    )

    if plan is None:
        return None

    for var, value in vars(new_plan).items():
        if var != "rules":
            setattr(plan, var, value) if value else None
        else:
            setattr(
                plan, var, [db.query(models.Rule).get(v) for v in value]
            ) if value else None

    db.add(plan)
    db.commit()
    db.refresh(plan)
    return s.PlanOut.from_orm(plan)


@router.delete(
    "/connections/{conn_id}/discovery/plans/{id}",
    response_model=s.PlanDeleteOut,
)
async def delete(conn_id: int, id: int, db: Session = Depends(get_db)):
    plan = (
        db.query(models.Plan)
        .filter(models.Connection.id == conn_id, models.Plan.id == id)
        .one()
    )
    db.delete(plan)
    db.commit()
    return s.PlanDeleteOut.from_orm(plan)


@router.put(
    "/connections/{conn_id}/discovery/plans/{id}/run",
    tags=["Plans"],
    response_model=s.PlanInstanceOut,
)
def run(conn_id: int, id: int, db: Session = Depends(get_db)):

    plan = (
        db.query(models.Plan)
        .filter(models.Connection.id == conn_id, models.Plan.id == id)
        .one()
    )
    plan.status = "running"
    db.add(plan)

    plan_instance: models.PlanInstance = plan.get_new_instance()
    db.add(plan_instance)
    db.commit()
    db.refresh(plan_instance)
    task_id = start_plan.delay(conn_id, plan_instance.id)
    plan_instance.task_id = str(task_id)
    db.add(plan_instance)
    db.commit()
    db.refresh(plan_instance)
    return s.PlanInstanceOut.from_orm(plan_instance)


@router.get(
    "/connections/{conn_id}/discovery/plans/{id}/last-instance",
    response_model=s.PlanInstanceOut,
)
async def get_last_instance(
    conn_id: int, id: int, db: Session = Depends(get_db)
):
    plan_instance = (
        db.query(models.PlanInstance)
        .filter(models.Connection.id == conn_id, models.Plan.id == id)
        .order_by(models.PlanInstance.created_on.desc())
        .first()
    )
    return s.PlanInstanceOut.from_orm(plan_instance)

