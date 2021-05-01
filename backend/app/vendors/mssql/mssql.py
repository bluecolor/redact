import json
from typing import Any, List, Optional

import pymssql
from pydantic import parse_obj_as
from pydash.arrays import chunk

import app.models.schemas as s
from app.models.orm.connection import Connection
from app.models.schemas.mssql import MaskedColumn, SqlServerUser
from app.vendors import register_vendor
from app.vendors.base import Vendor

from . import queries as q
from .discovery import DiscoveryMixin
from .mask import MaskMixin


class SqlServer(Vendor, MaskMixin, DiscoveryMixin):
    @classmethod
    def type(cls):
        return "mssql"

    def __init__(self, config: Connection, *args, **kwargs) -> None:
        super(SqlServer, self).__init__(config, *args, **kwargs)

    def connect(self) -> Any:
        return pymssql.connect(
            server=self.config.host,
            user=self.config.username,
            password=self.config.password_plain,
            database=self.config.database,
            port=self.config.port,
        )

    def get_tables(self, schema_name: Optional[str]) -> List[s.Table]:
        query = q.tables(schema_name)
        print(query)
        return parse_obj_as(List[s.Table], self.queryall(query))

    def get_schemas(self) -> List[s.Schema]:
        query = q.schemas()
        return parse_obj_as(List[s.Schema], self.queryall(query))

    def get_columns(
        self, schema_name: Optional[str], table_name: Optional[str],
    ) -> List[s.Column]:
        query = q.columns(schema_name, table_name)
        return parse_obj_as(List[s.Column], self.queryall(query))

    def get_table_packs(
        self, schemas: List[str], pack_count: int
    ) -> List[List[s.Table]]:
        query = q.tables_in_schemas(schemas)
        tables = parse_obj_as(List[s.Table], self.queryall(query))
        return chunk(tables, pack_count)

    def search(self, search_str: str) -> List[s.MetadataOut]:
        schemas = []
        try:
            options: dict = json.loads(self.options)
            schemas = options.get("search", {}).get("schemas", [])
        except:
            ...

        query = q.tables_and_columns_in_schemas(search_str, schemas)
        return parse_obj_as(List[s.MetadataOut], self.queryall(query))

    def get_sample(
        self, schema_name: str, table_name: str, column_name: str
    ) -> List[dict]:
        query = q.sample(schema_name, table_name, column_name)
        return self.queryall(query)

    def get_users(self) -> List[SqlServerUser]:
        query = q.users()
        return parse_obj_as(List[SqlServerUser], self.queryall(query))


register_vendor(SqlServer)
