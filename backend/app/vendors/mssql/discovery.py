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

    def search_table_data(self, table: Table, rule: Rule) -> SearchResult:
        ...

    def search_table_metadata(self, table: Table, rule: Rule) -> SearchResult:
        ...
