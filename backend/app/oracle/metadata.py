from typing import Any, List, Optional
from .base import connect, fetchall, queryall
import app.models.orm as models
import app.models.pydantic as schemas
from . import queries as q
from pydantic import parse_obj_as


def get_all_tables(
    connection: models.Connection, owner: Optional[str]
) -> List[schemas.Table]:
    query = q.all_tables(owner=owner)
    return parse_obj_as(List[schemas.Table], queryall(connection, query))


def get_all_tab_cols(
    connection: models.Connection,
    owner: Optional[str],
    table_name: Optional[str],
) -> List[schemas.Column]:
    query = q.all_tab_cols(owner, table_name)
    return parse_obj_as(List[schemas.Column], queryall(connection, query))

