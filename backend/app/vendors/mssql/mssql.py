from typing import Any, List, Optional
import pymssql
from app.models.orm import Connection
from app.vendors.base import Vendor
from app.vendors import register_vendor
import app.models.schemas as s
from app.models.schemas.mssql import MaskedColumn
from . import queries as q
from pydantic import parse_obj_as
from .mask import MaskMixin


class SqlServer(Vendor, MaskMixin):
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
        print(query)
        return parse_obj_as(List[s.Column], self.queryall(query))

    def get_table_packs(
        self, schemas: List[str], pack_count: int
    ) -> List[List[s.Table]]:
        ...

    def search(self, search_str: str) -> List[s.MetadataOut]:
        ...

    def get_sample(
        self, schema_name: str, table_name: str, column_name: str
    ) -> List[dict]:
        ...

    def get_masked_columns(
        self, schema_name: str, table_name: str
    ) -> List[MaskedColumn]:
        query = q.masked_columns(schema_name, table_name)
        return parse_obj_as(List[MaskedColumn], self.queryall(query))


register_vendor(SqlServer)
