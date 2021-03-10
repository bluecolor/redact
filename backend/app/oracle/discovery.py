from typing import List
import json

from sqlalchemy.sql.expression import table
from app.models.orm import Connection,Rule, Discovery
from .base import connect
from . import queries as q
from .base import queryall


def search(connection: Connection, schemas: List[str],  rule: Rule) -> Discovery :
    print(f"Rule type: {rule.type}")
    if rule.type == 'metadata':
        yield from search_metadata(connection, schemas, rule)
    elif rule.type == 'data':
        yield from search_data(connection, schemas, rule)

def search_metadata(connection: Connection, schemas: List[str], rule: Rule) -> Discovery:
    for schema in schemas:
        query = q.columns_like(schema, rule.expression)
        print(f"Query {query}")
        results = queryall(connection, query)
        for r in results:
            yield Discovery(
                rule=rule,
                schema_name=schema,
                table_name=r['table_name'],
                column_name=r['column_name'])


def search_data(connection: Connection, schemas: List[str], rule: Rule) -> Discovery:
    return []