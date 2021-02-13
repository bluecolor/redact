from typing import Any

from pydantic import parse_obj_as
from .base import connect
import app.models.orm as models
import app.models.pydantic as schemas
from . import queries as q

# cursor.callproc("so_test", keywordParameters = dict(p2 = "Y", p3 = "Z"))


def get_redaction_policies(
    connection: models.Connection, owner: str = None, table: str = None
) -> Any:
    with connect(connection) as conn:
        cursor = conn.cursor()
        cursor.execute(q.redaction_policies(owner=owner, table=table))
        result = cursor.fetchall()
        cursor.close()

    return result


def add_policy(connection: models.Connection, policy: dict):
    with connect(connection) as conn:
        cursor = conn.cursor()
        cursor.callproc("dbms_redact.add_policy", keywordParameters=policy)
        cursor.close()
    return parse_obj_as(schemas.Policy, policy)

