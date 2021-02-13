from typing import Any, List, Optional

from pydantic import parse_obj_as
from .base import connect
import app.models.orm as models
import app.models.pydantic as schemas
from . import queries as q
from .base import callproc, queryall


DBMS_REDACT = dict(
    none=0,
    full=1,
    partial=2,
    format_preserving=3,
    random=4,
    regexp=5,
    nullify=6,
    regexp_width=7,
    add_column=1,
    drop_column=2,
    modify_expression=3,
    modify_column=4,
    set_policy_description=6,
    set_column_description=6,
)


def get_policies(
    connection: models.Connection,
    owner: Optional[str] = None,
    table_name: Optional[str] = None,
) -> List[schemas.RedactionPolicyOut]:
    query = q.redaction_policies(owner=owner, table_name=table_name)
    return parse_obj_as(
        List[schemas.RedactionPolicyOut], queryall(connection, query)
    )


def get_expressions(
    connection: models.Connection,
    object_owner: Optional[str] = None,
    object_name: Optional[str] = None,
) -> List[schemas.RedactionExpressionOut]:
    query = q.redaction_expressions(object_owner, object_name)
    return parse_obj_as(
        List[schemas.RedactionExpressionOut], queryall(connection, query)
    )


def get_columns(
    connection: models.Connection,
    object_owner: Optional[str] = None,
    object_name: Optional[str] = None,
) -> List[schemas.RedactionColumnOut]:
    query = q.redaction_columns(object_owner, object_name)
    return parse_obj_as(
        List[schemas.RedactionColumnOut], queryall(connection, query)
    )


def add_policy(connection: models.Connection, policy: dict):
    callproc(connection, "dbms_redact.add_policy", policy)


def drop_policy(connection: models.Connection, policy: dict):
    callproc(connection, "dbms_redact.drop_policy", policy)


def alter_policy(connection: models.Connection, policy: dict):
    callproc(connection, "dbms_redact.alter_policy", policy)


def create_policy_expression(
    connection: models.Connection, policy_expression: dict
):
    callproc(
        connection, "dbms_redact.create_policy_expression", policy_expression
    )


def apply_policy_expr_to_col(connection: models.Connection, payload: dict):
    callproc(connection, "dbms_redact.apply_policy_expr_to_col", payload)


def update_policy_expression(connection: models.Connection, payload: dict):
    callproc(connection, "dbms_redact.update_policy_expression", payload)


def drop_policy_expression(connection: models.Connection, payload: dict):
    callproc(connection, "dbms_redact.drop_policy_expression", payload)
