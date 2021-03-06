from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas as schemas
from .base import router
from app.database import get_db
from app.oracle import redact
from pydantic import parse_obj_as


@router.get(
    "/connections/{conn_id}/discovery/rules",
    response_model=List[schemas.RuleOut],
)
def get_rules(conn_id: int, db: Session = Depends(get_db)) -> List[schemas.RuleOut]:
    rules = db.query(models.Rule).filter(models.Rule.connection_id == conn_id).all()
    return parse_obj_as(List[schemas.RuleOut], rules)


@router.post(
    "/connections/{conn_id}/discovery/rules", tags=["Rules"], response_model=schemas.RuleOut
)
def create_rule(conn_id: int, rule: schemas.RuleCreateIn, db: Session = Depends(get_db)):
    new_rule: models.Rule = models.Rule(**{**rule.dict(), "connection_id": conn_id})
    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)

    return schemas.RuleOut.from_orm(new_rule)


@router.get(
    "/connections/{conn_id}/discovery/plans",
    response_model=List[schemas.PlanOut],
)
def get_plans(conn_id: int, db: Session = Depends(get_db)) -> List[schemas.PlanOut]:
    rules = db.query(models.Plan).filter(models.Plan.connection_id == conn_id).all()
    return parse_obj_as(List[schemas.PlanOut], rules)



@router.post(
    "/connections/{conn_id}/discovery/plans", tags=["Plans"], response_model=schemas.PlanOut
)
def create_plan(conn_id: int, plan: schemas.PlanCreateIn, db: Session = Depends(get_db)):
    rules = db.query(models.Rule).filter(models.Rule.id.in_(plan.rules)).all()
    new_plan: models.Plan = models.Plan(**{**plan.dict(), "connection_id": conn_id, "rules": rules})
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return schemas.PlanOut.from_orm(new_plan)


