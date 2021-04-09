from app.models.schemas.discovery import SearchResult
from typing import List

from sqlalchemy.sql.expression import column, table
from app.models.orm import Connection, Discovery
from app.models.schemas import Rule, Table
import app.models.schemas.discovery as sd
from .base import connect
from . import queries as q
from .base import queryall


def _build_data_search_query(
    connection: Connection, *, schema: str, table: str, rule: Rule
) -> str:
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

    return query


def search_tables(
    connection: Connection, tables: List[Table], rules: List[Rule]
) -> sd.SearchResult:
    for t, r in [(table, rule) for rule in rules for table in tables]:
        if r.type == "metadata":
            yield from search_table_metadata(connection, table=t, rule=r)
        elif r.type == "data":
            yield from search_table_data(connection, table=t, rule=r)


def search_table_metadata(
    connection: Connection, table: Table, rule: Rule
) -> sd.SearchResult:
    query = q.columns_like(
        schema=table.owner,
        table_name=table.table_name,
        expression=rule.expression,
    )
    print(f"m => {table.owner}.{table.table_name}")
    results = queryall(connection, query)
    for r in results:
        discovery = sd.Discovery(
            rule=rule,
            schema_name=table.owner,
            table_name=table.table_name,
            column_name=r["column_name"],
        )
        yield sd.SearchResult(hit=True, table=table, discovery=discovery)

    if len(results) == 0 or (
        len(results) == 1
        and len(
            [
                is_match
                for _, is_match in results[0].items()
                if is_match is not None
            ]
        )
        == 0
    ):
        yield sd.SearchResult(hit=False, table=table)


def search_table_data(
    connection: Connection, table: Table, rule: Rule
) -> sd.SearchResult:
    query = _build_data_search_query(
        connection, schema=table.owner, table=table.table_name, rule=rule
    )
    print(f"d => {table.owner}.{table.table_name}")
    results: List[dict] = []
    try:
        results = queryall(connection, query, lower_keys=False)
    except:
        yield SearchResult(hit=False, table=table)

    for record in results:
        for col_name, is_match in record.items():
            if is_match == 1:
                discovery = sd.Discovery(
                    rule=rule,
                    schema_name=table.owner,
                    table_name=table.table_name,
                    column_name=col_name,
                )
                yield SearchResult(hit=True, table=table, discovery=discovery)

    if len(results) == 0 or (
        len(results) == 1
        and len(
            [
                is_match
                for _, is_match in results[0].items()
                if is_match is not None
            ]
        )
        == 0
    ):
        yield SearchResult(hit=False, table=table)

