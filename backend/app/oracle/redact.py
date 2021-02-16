from typing import Any, List, Optional

from pydantic import parse_obj_as
from .base import connect
import app.models.orm as models
import app.models.schemas as schemas
from . import queries as q
from .base import callproc, queryall


DBMS_REDACT = dict(
    NONE=0,
    FULL=1,
    PARTIAL=2,
    FORMAT_PRESERVING=3,
    RANDOM=4,
    REGEXP=5,
    NULLIFY=6,
    REGEXP_WIDTH=7,
    ADD_COLUMN=1,
    DROP_COLUMN=2,
    MODIFY_EXPRESSION=3,
    MODIFY_COLUMN=4,
    SET_POLICY_DESCRIPTION=5,
    SET_COLUMN_DESCRIPTION=6,
)


def get_function_types() -> List[schemas.RedactFunctionTypeOut]:
    return parse_obj_as(
        List[schemas.RedactFunctionTypeOut],
        [
            dict(function_type=DBMS_REDACT["NONE"], name="NONE"),
            dict(function_type=DBMS_REDACT["FULL"], name="FULL"),
            dict(function_type=DBMS_REDACT["PARTIAL"], name="PARTIAL"),
            dict(
                function_type=DBMS_REDACT["FORMAT_PRESERVING"],
                name="FORMAT_PRESERVING",
            ),
            dict(function_type=DBMS_REDACT["RANDOM"], name="RANDOM",),
            dict(function_type=DBMS_REDACT["REGEXP"], name="REGEXP",),
            dict(function_type=DBMS_REDACT["NULLIFY"], name="NULLIFY",),
            dict(
                function_type=DBMS_REDACT["REGEXP_WIDTH"], name="REGEXP_WIDTH",
            ),
        ],
    )


def get_actions() -> List[schemas.RedactActionOut]:
    return parse_obj_as(
        List[schemas.RedactActionOut],
        [
            dict(action=DBMS_REDACT["ADD_COLUMN"], name="ADD_COLUMN"),
            dict(action=DBMS_REDACT["DROP_COLUMN"], name="DROP_COLUMN"),
            dict(
                action=DBMS_REDACT["MODIFY_EXPRESSION"],
                name="MODIFY_EXPRESSION",
            ),
            dict(action=DBMS_REDACT["MODIFY_COLUMN"], name="MODIFY_COLUMN"),
            dict(
                action=DBMS_REDACT["SET_POLICY_DESCRIPTION"],
                name="SET_POLICY_DESCRIPTION",
            ),
            dict(
                action=DBMS_REDACT["SET_COLUMN_DESCRIPTION"],
                name="SET_COLUMN_DESCRIPTION",
            ),
        ],
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

def get_expression(connection: models.Connection, policy_expression_name: str) -> schemas.RedactionExpressionOut:
    query = q.redaction_expression(policy_expression_name)
    result = queryall(connection, query)
    if len(result) > 0:
        return parse_obj_as(schemas.RedactionExpressionOut, result[0])
    return None


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
