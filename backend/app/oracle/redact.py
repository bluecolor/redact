from typing import Any, List

from pydantic import parse_obj_as
from .base import connect
import app.models.orm as models
import app.models.pydantic as schemas
from . import queries as q
from .base import callproc, queryall


DBMS_REDACT = dict(
    nullify=1,
    none=0,
    full=1,
    partial=2,
    format_preserving=3,
    random=4,
    regexp=5,
    add_column=1,
    drop_column=2,
    modify_expression=3,
    modify_column=3,
    set_policy_description=4,
    set_column_description=5,
)


def get_redaction_policies(
    connection: models.Connection, owner: str = None, table: str = None
) -> Any:
    query = q.redaction_policies(owner=owner, table=table)
    return parse_obj_as(List[schemas.Policy], queryall(connection, query))


def add_policy(connection: models.Connection, policy: dict):
    callproc(connection, "dbms_redact.add_policy", policy)

