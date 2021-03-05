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
    "/discovery/rules",
    response_model=List[schemas.RuleOut],
)
def get_rules(db: Session = Depends(get_db)) -> List[schemas.RuleOut]:
    rules = db.query(models.Rule).all()
    return parse_obj_as(List[schemas.RuleOut], rules)


@router.post(
    "/discovery/rules", tags=["Rules"], response_model=schemas.RuleOut
)
def create_rule(rule: schemas.RuleCreateIn, db: Session = Depends(get_db)):
    new_rule: models.Rule = models.Rule(**rule.dict())
    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)

    return schemas.RuleOut.from_orm(new_rule)

