import json
from typing import Any, Optional, List

from app.models.orm import Connection
import cx_Oracle
from app.vendors.base import Vendor
from . import queries as q
from pydantic import parse_obj_as
import app.models.schemas as s
from pydash.arrays import chunk
from app.vendors import register_vendor
from .redaction import RedactionMixin
from .discovery import DiscoveryMixin

DBMS_REDACT = dict(
    NONE=0,
    FULL=1,
    PARTIAL=2,
    FORMAT_PRESERVING=3,
    RANDOM=4,
    REGEXP=5,
    NULLIFY=6,
    REGEXP_WIDTH=7,
    ADD_COLUMN=1,
    DROP_COLUMN=2,
    MODIFY_EXPRESSION=3,
    MODIFY_COLUMN=4,
    SET_POLICY_DESCRIPTION=5,
    SET_COLUMN_DESCRIPTION=6,
    REDACT_US_SSN_F5="VVVFVVFVVVV,VVV-VV-VVVV,X,1,5",
    REDACT_US_SSN_L4="VVVFVVFVVVV,VVV-VV-VVVV,X,6,9",
    REDACT_US_SSN_ENTIRE="VVVFVVFVVVV,VVV-VV-VVVV,X,1,9",
    REDACT_NUM_US_SSN_F5="9,1,5",
    REDACT_NUM_US_SSN_L4="9,6,9",
    REDACT_NUM_US_SSN_ENTIRE="9,1,9",
    REDACT_ZIP_CODE="VVVVV,VVVVV,X,1,5",
    REDACT_NUM_ZIP_CODE="9,1,5",
    REDACT_CCN16_F12="VVVVFVVVVFVVVVFVVVV,VVVV-VVVV-VVVV-VVVV,*,1,12",
    REDACT_DATE_MILLENNIUM="m1d1y2000",
    REDACT_DATE_EPOCH="m1d1y1970",
    REDACT_AMEX_CCN_FORMATTED="VVVVFVVVVVVFVVVVV,VVVV-VVVVVV-VVVVV,*,1,10",
    REDACT_AMEX_CCN_NUMBER="0,1,10",
    REDACT_SIN_FORMATTED="VVVFVVVFVVV,VVV-VVV-VVV,*,1,6",
    REDACT_SIN_NUMBER="9,1,6",
    REDACT_SIN_UNFORMATTED="VVVVVVVVV,VVVVVVVVV,*,1,6",
    REDACT_CCN_FORMATTED="VVVVFVVVVFVVVVFVVVV,VVVV-VVVV-VVVV-VVVV,*,1,12",
    REDACT_CCN_NUMBER="9,1,12",
    REDACT_NA_PHONE_FORMATTED="VVVFVVVFVVVV,VVV-VVV-VVVV,X,1,6",
    REDACT_NA_PHONE_NUMBER="0,4,10",
    REDACT_NA_PHONE_UNFORMATTED="VVVVVVVVVV,VVVVVVVVVV,X,4,10",
    REDACT_UK_NIN_FORMATTED="VVFVVFVVFVVFV,VV VV VV VV V,X,3,8",
    REDACT_UK_NIN_UNFORMATTED="VVVVVVVVV,VVVVVVVVV,X,3,8",
    RE_PATTERN_US_SSN="(\d\d\d)-(\d\d)-(\d\d\d\d)",
    RE_PATTERN_CC_L6_T4="(\d\d\d\d\d\d)(\d\d\d*)(\d\d\d\d)",
    RE_PATTERN_ANY_DIGIT="\d",
    RE_PATTERN_US_PHONE="(\(\d\d\d\)|\d\d\d)-(\d\d\d)-(\d\d\d\d)",
    RE_PATTERN_EMAIL_ADDRESS="([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,4})",
    RE_PATTERN_IP_ADDRESS="(\d{1,3}\.\d{1,3}\.\d{1,3})\.\d{1,3}",
    RE_PATTERN_AMEX_CCN=".*(\d\d\d\d\d)$",
    RE_PATTERN_CCN=".*(\d\d\d\d)$",
    RE_REDACT_CC_MIDDLE_DIGITS="\\1XXXXXX\3",
    RE_REDACT_WITH_SINGLE_X="X",
    RE_REDACT_WITH_SINGLE_1="1",
    RE_REDACT_US_PHONE_L7="\\1-XXX-XXXX",
    RE_REDACT_EMAIL_NAME="xxxx@\2",
    RE_REDACT_EMAIL_DOMAIN="\\1@xxxxx.com",
    RE_REDACT_EMAIL_ENTIRE="xxxx@xxxxx.com",
    RE_REDACT_IP_L3="\\1.999",
    RE_REDACT_AMEX_CCN="**********\\1",
    RE_REDACT_CCN="************\\1",
    RE_BEGINNING=1,
    RE_ALL=0,
    RE_FIRST=1,
    RE_CASE_SENSITIVE="c",
    RE_CASE_INSENSITIVE="i",
    RE_MULTIPLE_LINES="m",
    RE_NEWLINE_WILDCARD="n",
    RE_IGNORE_WHITESPACE="x",
)


class Oracle(Vendor, RedactionMixin, DiscoveryMixin):
    @classmethod
    def type(cls):
        return "oracle"

    def __init__(self, config: Connection, *args, **kwargs) -> None:
        super(Oracle, self).__init__(config, *args, **kwargs)

    def connect(self) -> Any:
        return cx_Oracle.connect(
            self.config.username, self.config.password_plain, self.config.dsn
        )

    def get_tables(self, schema_name: Optional[str]) -> List[s.Table]:
        query = q.tables(schema_name)
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

    def get_users(self) -> List[Any]:
        ...


register_vendor(Oracle)
