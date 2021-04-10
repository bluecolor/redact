from typing import Any, List, Optional
import pymssql
from app.models.orm import Connection
from app.vendors.base import Vendor
from app.vendors import register_vendor
import app.models.schemas as s


class SqlServer(Vendor):
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
        ...

    def get_schemas(self) -> List[s.Schema]:
        ...

    def get_columns(
        self, schema_name: Optional[str], table_name: Optional[str],
    ) -> List[s.Column]:
        ...

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


register_vendor(SqlServer)
