from app.models.schemas.discovery import SearchResult
from typing import List

from sqlalchemy.sql.expression import column, table
from app.models.schemas import Rule, Table
import app.models.schemas.discovery as sd
from . import queries as q
from app.vendors.base import VendorABC


class DiscoveryMixin(VendorABC):
    def __init__(self) -> None:
        super().__init__()

    def _build_data_search_query(
        self, *, schema_name: str, table_name: str, rule: Rule
    ) -> str:
        # todo: add more data types
        q: str = f"""
            select column_name as name
            from all_tab_cols
            where owner = '{schema_name}' and table_name = '{table_name}'
            and data_type in ('NUMBER', 'VARCHAR2', 'CHAR')
        """

        columns = self.queryall(q)
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
                select * from {schema_name}.{table_name} order by dbms_random.random
            ) where rownum < 5000 and ({' or '.join(filter_expressions)})
        """

        return query

    def search_table_metadata(
        self, table: Table, rule: Rule
    ) -> sd.SearchResult:
        query = q.columns_like(
            schema=table.schema_name,
            table_name=table.table_name,
            expression=rule.expression,
        )
        print(f"m => {table.schema_name}.{table.table_name}")
        results = self.queryall(query)
        for r in results:
            discovery = sd.Discovery(
                rule=rule,
                schema_name=table.schema_name,
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

    def search_table_data(self, table: Table, rule: Rule) -> sd.SearchResult:
        query = self._build_data_search_query(
            schema_name=table.schema_name,
            table_name=table.table_name,
            rule=rule,
        )
        print(f"d => {table.schema_name}.{table.table_name}")
        results: List[dict] = []
        try:
            results = self.queryall(query, lower_keys=False)
        except:
            yield SearchResult(hit=False, table=table)

        for record in results:
            for col_name, is_match in record.items():
                if is_match == 1:
                    discovery = sd.Discovery(
                        rule=rule,
                        schema_name=table.schema_name,
                        table_name=table.table_name,
                        column_name=col_name,
                    )
                    yield SearchResult(
                        hit=True, table=table, discovery=discovery
                    )

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

