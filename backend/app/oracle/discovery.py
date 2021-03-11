from typing import List, Any
import json

from sqlalchemy.sql.expression import column, table
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
    query: str = f"""select owner, table_name as name from all_tables where owner in ({','.join([f"'{s}'" for s in schemas])})"""
    tables: List[dict] = queryall(connection, query)
    for t in tables:
        query, _ = _build_data_search_query(connection, schema=t['owner'], table=t['name'], rule=rule)
        print(query)
        results: List[dict] = queryall(connection, query)
        for record in results:
            for col_name, is_match in record.items():
                if is_match == 1:
                    yield Discovery(
                    rule=rule,
                    schema_name=t['owner'],
                    table_name=t['name'],
                    column_name=col_name)


def _build_data_search_query(connection: Connection, *, schema: str, table: str, rule: Rule) -> str:
    # todo: add more data types
    q: str = f"""
        select column_name as name
        from all_tab_cols
        where owner = '{schema}' and table_name = '{table}'
        and data_type in ('NUMBER', 'VARCHAR2', 'CHAR')
    """
    columns = queryall(connection, q)
    select_expressions = []
    filter_expressions = []
    for c in columns:
        se = f"max(case when regexp_instr({c['name']}, '{rule.expression}', 1, 1, 0, 'i') > 0 then 1 else 0 end) as {c['name']}"
        select_expressions.append(se)
        fe = f"regexp_like({c['name']}, '{rule.expression}', 'i')"
        filter_expressions.append(fe)

    # todo: rownum from rule
    query = f"""
        select {' , '.join(select_expressions)} from (
            select * from {schema}.{table} order by dbms_random.random
        ) where rownum < 5000 and ({' or '.join(filter_expressions)})
    """

    return query, columns