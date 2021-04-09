from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.oracle.redact as s
from .base import router
from app.database import get_db
from app.vendor.oracle import redact


@router.get(
    "/connections/{conn_id}/redact/expressions",
    response_model=List[s.ExpressionOut],
)
def get_all(
    conn_id: int,
    object_owner: Optional[str] = None,
    object_name: Optional[str] = None,
    db: Session = Depends(get_db),
) -> List[s.ExpressionOut]:
    connection = db.query(models.Connection).get(conn_id)
    return redact.get_expressions(connection, object_owner, object_name)


@router.get(
    "/connections/{conn_id}/redact/expressions/{name}",
    response_model=s.ExpressionOut,
)
def get_one(
    conn_id: int, name: str = None, db: Session = Depends(get_db),
) -> s.ExpressionOut:
    connection = db.query(models.Connection).get(conn_id)
    return redact.get_expression(connection, name)


@router.post(
    "/connections/{conn_id}/redact/expressions", response_model=bool,
)
def create(
    policy_expression: s.ExpressionCreateIn,
    conn_id: int,
    db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.create_policy_expression(connection, policy_expression.dict())
    return True


@router.put(
    "/connections/{conn_id}/redact/expressions/{name}", response_model=bool,
)
def update(
    name: str,
    payload: s.ExpressionUpdateIn,
    conn_id: int,
    db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.update_policy_expression(connection, payload.dict())
    return True


@router.delete(
    "/connections/{conn_id}/redact/expressions/{name}", response_model=bool,
)
def delete(conn_id: int, name=str, db: Session = Depends(get_db)):
    connection = db.query(models.Connection).get(conn_id)
    redact.drop_policy_expression(connection, {"policy_expression_name": name})
    return True


@router.put(
    "/connections/{conn_id}/redact/expressions/{policy_expression_name}/apply-to-column",
    response_model=bool,
)
def apply(
    payload: s.ExpressionApplyIn,
    conn_id: int,
    policy_expression_name: str,
    db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.apply_policy_expr_to_col(connection, payload.dict())
    return True

