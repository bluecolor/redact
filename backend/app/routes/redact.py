from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
from app.models.orm.connection import Connection
import app.models.pydantic as schemas
from .base import router
from app.database import get_db
from app.oracle import redact


@router.post(
    "/connections/{conn_id}/redact/policies", response_model=bool,
)
def add_policy(
    policy: schemas.PolicyIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.add_policy(connection, policy.dict())
    return True


@router.delete(
    "/connections/{conn_id}/redact/policies", response_model=bool,
)
def drop_policy(
    policy: schemas.DropPolicyIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.drop_policy(connection, policy.dict())
    return True


@router.put(
    "/connections/{conn_id}/redact/policies", response_model=bool,
)
def alter_policy(
    policy: schemas.AlterPolicyIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.alter_policy(connection, policy.dict())
    return True


@router.post(
    "/connections/{conn_id}/redact/policies/expressions", response_model=bool,
)
def alter_policy(
    policy_expression: schemas.CreatePolicyExpressionIn,
    conn_id: int,
    db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.create_policy_expression(connection, policy_expression.dict())
    return True


@router.put(
    "/connections/{conn_id}/redact/policies/expressions", response_model=bool,
)
def update_policy_expression(
    payload: schemas.UpdatePolicyExpressionIn,
    conn_id: int,
    db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.update_policy_expression(connection, payload.dict())
    return True


@router.delete(
    "/connections/{conn_id}/redact/policies/expressions", response_model=bool,
)
def drop_policy_expression(
    conn_id: int, name=str, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.drop_policy_expression(connection, {"policy_expression_name": name})
    return True


@router.post(
    "/connections/{conn_id}/redact/policies/expressions/apply",
    response_model=bool,
)
def apply_policy_expr_to_col(
    payload: schemas.ApplyPolicyExprToColIn,
    conn_id: int,
    db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.apply_policy_expr_to_col(connection, payload.dict())
    return True
