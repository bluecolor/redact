from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.oracle.redact as s
from .base import router
from app.database import get_db
from app.vendors.oracle import Oracle


@router.get(
    "/connections/{conn_id}/oracle/redact/expressions",
    response_model=List[s.ExpressionOut],
)
def get_all(
    conn_id: int,
    object_owner: Optional[str] = None,
    object_name: Optional[str] = None,
    db: Session = Depends(get_db),
) -> List[s.ExpressionOut]:
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    return oracle.get_expressions(object_owner, object_name)


@router.get(
    "/connections/{conn_id}/oracle/redact/expressions/{name}",
    response_model=s.ExpressionOut,
)
def get_one(
    conn_id: int, name: str = None, db: Session = Depends(get_db),
) -> s.ExpressionOut:
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    return oracle.get_expression(name)


@router.post(
    "/connections/{conn_id}/oracle/redact/expressions", response_model=bool,
)
def create(
    policy_expression: s.ExpressionCreateIn,
    conn_id: int,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    oracle.create_policy_expression(policy_expression.dict())
    return True


@router.put(
    "/connections/{conn_id}/oracle/redact/expressions/{name}",
    response_model=bool,
)
def update(
    name: str,
    payload: s.ExpressionUpdateIn,
    conn_id: int,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    oracle.update_policy_expression(payload.dict())
    return True


@router.delete(
    "/connections/{conn_id}/oracle/redact/expressions/{name}",
    response_model=bool,
)
def delete(conn_id: int, name=str, db: Session = Depends(get_db)):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    oracle.drop_policy_expression({"policy_expression_name": name})
    return True


@router.put(
    "/connections/{conn_id}/oracle/redact/expressions/{policy_expression_name}/apply-to-column",
    response_model=bool,
)
def apply(
    payload: s.ExpressionApplyIn,
    conn_id: int,
    policy_expression_name: str,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    oracle.apply_policy_expr_to_col(payload.dict())
    return True

