from typing import Any, List
from .base import connect, fetchall
import app.models.orm as models
import app.models.pydantic as schemas
from . import queries as q
from pydantic import parse_obj_as


def get_all_tables(
    connection: models.Connection, owner: str = None
) -> List[schemas.Table]:
    with connect(connection=connection) as conn:
        cursor = conn.cursor()
        cursor.execute(q.all_tables(owner=owner))
        result = fetchall(cursor=cursor)
        cursor.close()

    return parse_obj_as(List[schemas.Table], result)
