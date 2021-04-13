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
            select
                c.name column_name
            from
                sys.columns c,
                sys.tables 	t,
                sys.schemas s,
                sys.types tp
            where
                tp.name in ('text', 'int', 'char', 'varchar') and
                tp.user_type_id = c.user_type_id and
                s.schema_id  = t.schema_id and
                t.object_id  = c.object_id and
                t.name = '{table_name}' and
                s.name = '{schema_name}'
        """

        columns = self.queryall(q)
        select_expressions = []
        filter_expressions = []
        for c in columns:
            se = f"""max(case when patindex('%{c["name"]}%', '{rule.expression}') != 0 then 1 else 0 end) as {c['name']}"""
            select_expressions.append(se)
            fe = f"""patindex('%{c["name"]}%', '{rule.expression}') != 0"""
            filter_expressions.append(fe)

        # todo: rownum from rule
        query = f"""
            select {' , '.join(select_expressions)} from (
                select top(5000) * from {schema_name}.{table_name} order by newid()
            ) q where ({' or '.join(filter_expressions)})
        """

        return query

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

    def search_table_metadata(
        self, table: Table, rule: Rule
    ) -> sd.SearchResult:
        query = q.columns_like(
            schema=table.schema_name,
            table_name=table.table_name,
            expression=rule.expression,
        )
        print(query)
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
