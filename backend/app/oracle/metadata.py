import json
from typing import Any, List, Optional
from sqlalchemy.sql.expression import table
from sqlalchemy.sql.functions import mode

from sqlalchemy.util.langhelpers import constructor_copy
from .base import connect, fetchall, queryall
import app.models.orm as models
import app.models.schemas.metadata as s
from . import queries as q
from pydantic import parse_obj_as
from pydash.arrays import chunk


def get_all_tables(
    connection: models.Connection, owner: Optional[str]
) -> List[s.Table]:
    query = q.all_tables(owner=owner)
    return parse_obj_as(List[s.Table], queryall(connection, query))


def get_object_owners(connection: models.Connection) -> List[s.Table]:
    query = q.all_object_owners()
    return parse_obj_as(List[s.ObjectOwner], queryall(connection, query))


def get_schemas(connection: models.Connection) -> List[s.SchemaOut]:
    query = q.all_schemas()
    return parse_obj_as(List[s.SchemaOut], queryall(connection, query))


def get_all_tab_cols(
    connection: models.Connection,
    owner: Optional[str],
    table_name: Optional[str],
) -> List[s.Column]:
    query = q.all_tab_cols(owner, table_name)
    return parse_obj_as(List[s.Column], queryall(connection, query))


def get_table_packs(
    connection: models.Connection, schemas: List[str], pack_count: int
) -> List[List[s.Table]]:
    query = q.all_tables_in_schemas(schemas)
    tables = parse_obj_as(List[s.Table], queryall(connection, query))
    return chunk(tables, pack_count)


def search(connection: models.Connection, query: str) -> List[s.SearchOut]:
    schemas = []
    try:
        options: dict = json.loads(connection.options)
        schemas = options.get("search", {}).get("schemas", [])
    except:
        ...
    query = q.all_tabs_and_cols(query, schemas)
    return parse_obj_as(List[s.SearchOut], queryall(connection, query))


def get_col_sample_data(
    connection: models.Connection,
    schema_name: str,
    table_name: str,
    column_name: str,
) -> List[dict]:
    query = q.column_sample(schema_name, table_name, column_name)
    return queryall(connection, query)
