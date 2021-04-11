from typing import Any, List, Optional
from app.models.schemas.mssql import MaskingFunction, MaskIn
from pydantic import parse_obj_as
from app.vendors.base import VendorABC

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
