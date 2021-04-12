from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.oracle.redact as s
import app.models.schemas.metadata as ms
from app.vendors.oracle.oracle import Oracle
from .base import router
from app.database import get_db
import pydash
from app.vendors.oracle import Oracle


@router.post(
    "/connections/{conn_id}/oracle/redact/ask/columns",
    response_model=List[s.ColumnAnswerOut],
)
def ask_columns(
    conn_id: int, columns: List[ms.ColumnIn], db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    oracle: Oracle = connection.get_vendor()
    expressions = oracle.get_expressions_in_columns(columns)
    red_columns = oracle.get_columns_in_columns(columns)
    answers: List[s.ColumnAnswerOut] = []

    for c in columns:
        answer: s.ColumnAnswerOut = s.ColumnAnswerOut(
            owner=c.schema_name,
            table_name=c.table_name,
            column_name=c.column_name,
        )
        answer.column = pydash.find(
            red_columns,
            lambda x: x.object_owner == c.schema_name
            and x.object_name == c.table_name
            and x.column_name == c.column_name,
        )
        answer.expression = pydash.find(
            expressions,
            lambda x: x.object_owner == c.schema_name
            and x.object_name == c.table_name
            and x.column_name == c.column_name,
        )
        answers.append(answer)

    return answers


@router.get(
    "/connections/{conn_id}/oracle/redact/ask/policy",
    response_model=dict,  # todo
)
def ask_policy(
    conn_id: int,
    schema_name: str,
    table_name: str,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    policies = oracle.get_policies(schema_name, table_name)

    if len(policies) > 0:
        return {"policy": policies[0]}

    return {"policy": None}


@router.get(
    "/connections/{conn_id}/oracle/redact/ask/expression",
    response_model=dict,  # todo
)
def ask_expression(
    conn_id: int,
    schema_name: str,
    table_name: str,
    column_name: str,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    expressions = oracle.get_expressions(schema_name, table_name, column_name)

    if len(expressions) > 0:
        return {"expression": expressions[0]}

    return {"expression": None}


@router.get(
    "/connections/{conn_id}/oracle/redact/ask/info",
    response_model=dict,  # todo
)
def ask_redaction_info(
    conn_id: int,
    schema_name: str,
    table_name: str,
    column_name: Optional[str] = None,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    expressions = oracle.get_expressions(schema_name, table_name, column_name)
    redaction_columns = oracle.get_expressions(
        schema_name, table_name, column_name
    )
    policies = oracle.get_policies(schema_name, table_name)

    return {
        "expressions": expressions,
        "redaction_columns": redaction_columns,
        "policies": policies,
    }
