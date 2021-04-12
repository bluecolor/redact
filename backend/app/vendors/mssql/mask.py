from typing import Any, List, Optional
from app.models.schemas.mssql import MaskingFunction, MaskIn, MaskedColumn
from pydantic import parse_obj_as
from app.vendors.base import VendorABC
from . import queries as q

MASKING_FUNCTIONS = [
    {"title": "Default", "name": "default"},
    {"title": "Email", "name": "email"},
    {
        "title": "Random",
        "name": "random",
        "args": "[start range], [end range]",
    },
    {
        "title": "Cusom String",
        "name": "partial",
        "args": "prefix,[padding],suffix",
    },
]


class MaskMixin(VendorABC):
    @classmethod
    def masking_functions(cls) -> List[MaskingFunction]:
        return parse_obj_as(List[MaskingFunction], MASKING_FUNCTIONS)

    def add_mask(self, mask: MaskIn):
        stmt = f"""
            ALTER TABLE {mask.schema_name}.{mask.table_name}
     	    ALTER COLUMN {mask.column_name}
            ADD MASKED WITH (FUNCTION = '{mask.func}({mask.args if mask.args else ""})')

        """
        self.execute(stmt)

    def get_masked_columns(
        self, schema_name: str, table_name: str, column_name: str = None
    ) -> List[MaskedColumn]:
        query = q.masked_columns(schema_name, table_name, column_name)
        return parse_obj_as(List[MaskedColumn], self.queryall(query))

    def drop_mask(self, schema_name: str, table_name: str, column_name: str):
        stmt = f"""
            ALTER TABLE {schema_name}.{table_name}
     	    ALTER COLUMN {column_name}
            DROP MASKED
        """
        self.execute(stmt)

    def grant_unmask(
        self, username: str,
    ):
        stmt = f"""
            GRANT UNMASK TO {username}
        """
        self.execute(stmt)

    def revoke_unmask(
        self, username: str,
    ):
        stmt = f"""
            REVOKE UNMASK TO {username}
        """
        self.execute(stmt)
