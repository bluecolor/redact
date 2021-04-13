from typing import Any, List, Optional


from pydantic import parse_obj_as
from app.vendors.base import VendorABC
from app.models.schemas.oracle.redact.base import Expression
import app.models.orm as models
from app.models.orm import Connection
import app.models.schemas.oracle.redact as s
import app.models.schemas.metadata as ms
from . import queries as q

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


class RedactionMixin(VendorABC):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def function_parameters(cls) -> List[s.FunctionParametersOut]:

        return parse_obj_as(
            List[s.FunctionParametersOut],
            [
                dict(function_parameters=DBMS_REDACT["REDACT_US_SSN_F5"]),
                dict(function_parameters=DBMS_REDACT["REDACT_US_SSN_L4"]),
                dict(function_parameters=DBMS_REDACT["REDACT_US_SSN_ENTIRE"]),
                dict(function_parameters=DBMS_REDACT["REDACT_NUM_US_SSN_F5"]),
                dict(function_parameters=DBMS_REDACT["REDACT_NUM_US_SSN_L4"]),
                dict(
                    function_parameters=DBMS_REDACT["REDACT_NUM_US_SSN_ENTIRE"]
                ),
                dict(function_parameters=DBMS_REDACT["REDACT_ZIP_CODE"]),
                dict(function_parameters=DBMS_REDACT["REDACT_NUM_ZIP_CODE"]),
                dict(function_parameters=DBMS_REDACT["REDACT_CCN16_F12"]),
                dict(
                    function_parameters=DBMS_REDACT["REDACT_DATE_MILLENNIUM"]
                ),
                dict(function_parameters=DBMS_REDACT["REDACT_DATE_EPOCH"]),
                dict(
                    function_parameters=DBMS_REDACT[
                        "REDACT_AMEX_CCN_FORMATTED"
                    ]
                ),
                dict(
                    function_parameters=DBMS_REDACT["REDACT_AMEX_CCN_NUMBER"]
                ),
                dict(function_parameters=DBMS_REDACT["REDACT_SIN_FORMATTED"]),
                dict(function_parameters=DBMS_REDACT["REDACT_SIN_NUMBER"]),
                dict(
                    function_parameters=DBMS_REDACT["REDACT_SIN_UNFORMATTED"]
                ),
                dict(function_parameters=DBMS_REDACT["REDACT_CCN_FORMATTED"]),
                dict(function_parameters=DBMS_REDACT["REDACT_CCN_NUMBER"]),
                dict(
                    function_parameters=DBMS_REDACT[
                        "REDACT_NA_PHONE_FORMATTED"
                    ]
                ),
                dict(
                    function_parameters=DBMS_REDACT["REDACT_NA_PHONE_NUMBER"]
                ),
                dict(
                    function_parameters=DBMS_REDACT[
                        "REDACT_NA_PHONE_UNFORMATTED"
                    ]
                ),
                dict(
                    function_parameters=DBMS_REDACT["REDACT_UK_NIN_FORMATTED"]
                ),
                dict(
                    function_parameters=DBMS_REDACT[
                        "REDACT_UK_NIN_UNFORMATTED"
                    ]
                ),
                dict(function_parameters=DBMS_REDACT["RE_PATTERN_US_SSN"]),
                dict(function_parameters=DBMS_REDACT["RE_PATTERN_CC_L6_T4"]),
                dict(function_parameters=DBMS_REDACT["RE_PATTERN_ANY_DIGIT"]),
                dict(function_parameters=DBMS_REDACT["RE_PATTERN_US_PHONE"]),
                dict(
                    function_parameters=DBMS_REDACT["RE_PATTERN_EMAIL_ADDRESS"]
                ),
                dict(function_parameters=DBMS_REDACT["RE_PATTERN_IP_ADDRESS"]),
                dict(function_parameters=DBMS_REDACT["RE_PATTERN_AMEX_CCN"]),
                dict(function_parameters=DBMS_REDACT["RE_PATTERN_CCN"]),
                dict(
                    function_parameters=DBMS_REDACT[
                        "RE_REDACT_CC_MIDDLE_DIGITS"
                    ]
                ),
                dict(
                    function_parameters=DBMS_REDACT["RE_REDACT_WITH_SINGLE_X"]
                ),
                dict(
                    function_parameters=DBMS_REDACT["RE_REDACT_WITH_SINGLE_1"]
                ),
                dict(function_parameters=DBMS_REDACT["RE_REDACT_US_PHONE_L7"]),
                dict(function_parameters=DBMS_REDACT["RE_REDACT_EMAIL_NAME"]),
                dict(
                    function_parameters=DBMS_REDACT["RE_REDACT_EMAIL_DOMAIN"]
                ),
                dict(
                    function_parameters=DBMS_REDACT["RE_REDACT_EMAIL_ENTIRE"]
                ),
                dict(function_parameters=DBMS_REDACT["RE_REDACT_IP_L3"]),
                dict(function_parameters=DBMS_REDACT["RE_REDACT_AMEX_CCN"]),
                dict(function_parameters=DBMS_REDACT["RE_REDACT_CCN"]),
                dict(function_parameters=DBMS_REDACT["RE_BEGINNING"]),
                dict(function_parameters=DBMS_REDACT["RE_ALL"]),
                dict(function_parameters=DBMS_REDACT["RE_FIRST"]),
                dict(function_parameters=DBMS_REDACT["RE_CASE_SENSITIVE"]),
                dict(function_parameters=DBMS_REDACT["RE_CASE_INSENSITIVE"]),
                dict(function_parameters=DBMS_REDACT["RE_MULTIPLE_LINES"]),
                dict(function_parameters=DBMS_REDACT["RE_NEWLINE_WILDCARD"]),
                dict(function_parameters=DBMS_REDACT["RE_IGNORE_WHITESPACE"]),
            ],
        )

    @classmethod
    def function_types(cls) -> List[s.FunctionTypeOut]:
        return parse_obj_as(
            List[s.FunctionTypeOut],
            [
                dict(function_type=DBMS_REDACT["NONE"], name="NONE"),
                dict(function_type=DBMS_REDACT["FULL"], name="FULL"),
                dict(function_type=DBMS_REDACT["PARTIAL"], name="PARTIAL"),
                dict(
                    function_type=DBMS_REDACT["FORMAT_PRESERVING"],
                    name="FORMAT_PRESERVING",
                ),
                dict(function_type=DBMS_REDACT["RANDOM"], name="RANDOM",),
                dict(function_type=DBMS_REDACT["REGEXP"], name="REGEXP",),
                dict(function_type=DBMS_REDACT["NULLIFY"], name="NULLIFY",),
                dict(
                    function_type=DBMS_REDACT["REGEXP_WIDTH"],
                    name="REGEXP_WIDTH",
                ),
            ],
        )

    @classmethod
    def actions(cls) -> List[s.ActionOut]:
        return parse_obj_as(
            List[s.ActionOut],
            [
                dict(action=DBMS_REDACT["ADD_COLUMN"], name="ADD_COLUMN"),
                dict(action=DBMS_REDACT["DROP_COLUMN"], name="DROP_COLUMN"),
                dict(
                    action=DBMS_REDACT["MODIFY_EXPRESSION"],
                    name="MODIFY_EXPRESSION",
                ),
                dict(
                    action=DBMS_REDACT["MODIFY_COLUMN"], name="MODIFY_COLUMN"
                ),
                dict(
                    action=DBMS_REDACT["SET_POLICY_DESCRIPTION"],
                    name="SET_POLICY_DESCRIPTION",
                ),
                dict(
                    action=DBMS_REDACT["SET_COLUMN_DESCRIPTION"],
                    name="SET_COLUMN_DESCRIPTION",
                ),
            ],
        )

    def get_policies(
        self,
        object_owner: Optional[str] = None,
        object_name: Optional[str] = None,
    ) -> List[s.PolicyOut]:
        query = q.redaction_policies(object_owner, object_name)
        return parse_obj_as(List[s.PolicyOut], self.queryall(query))

    def get_policies_for_tables(
        self, tables: List[ms.Table]
    ) -> List[s.PolicyOut]:
        query = q.redaction_policies_for_tables(tables)
        return parse_obj_as(List[s.PolicyOut], self.queryall(query))

    def get_expressions_in_columns(
        self, columns: List[ms.ColumnIn]
    ) -> List[s.ExpressionOut]:
        query = q.redaction_expressions_in_columns(columns)
        return parse_obj_as(List[s.ExpressionOut], self.queryall(query))

    def get_columns_in_columns(
        self, columns: List[ms.ColumnIn]
    ) -> List[s.ColumnOut]:
        query = q.redaction_columns_in_columns(columns)
        return parse_obj_as(List[s.ColumnOut], self.queryall(query))

    def get_policy(
        self, object_owner: str, object_name: str, policy_name: str,
    ):
        query = q.redaction_policies(object_owner, object_name, policy_name)
        result = self.queryall(query)
        if len(result) == 1:
            return parse_obj_as(s.PolicyOut, result[0])
        if len(result) > 1:
            raise Exception("Multiple results found for policy")

        return None

    def get_policy_owners(self) -> List[ms.Schema]:
        query = q.redaction_policy_owners()
        result = self.queryall(query)
        return parse_obj_as(List[ms.Schema], result)

    def get_policy_tables(self, owner: str) -> List[ms.Table]:
        query = q.redaction_policy_tables(owner)
        result = self.queryall(query)
        return parse_obj_as(List[ms.Table], result)

    def get_expressions(
        self,
        object_owner: Optional[str] = None,
        object_name: Optional[str] = None,
        column_name: Optional[str] = None,
    ) -> List[s.ExpressionOut]:
        query = q.redaction_expressions(object_owner, object_name, column_name)
        return parse_obj_as(List[s.ExpressionOut], self.queryall(query))

    def get_expression(self, policy_expression_name: str) -> s.ExpressionOut:
        query = q.redaction_expression(policy_expression_name)
        result = self.queryall(query)
        if len(result) > 0:
            return parse_obj_as(s.ExpressionOut, result[0])
        return None

    def get_redaction_columns(
        self,
        object_owner: Optional[str] = None,
        object_name: Optional[str] = None,
        column_name: Optional[str] = None,
    ) -> List[s.ColumnOut]:
        query = q.redaction_columns(object_owner, object_name, column_name)
        return parse_obj_as(List[s.ColumnOut], self.queryall(query))

    def add_policy(self, policy: dict):
        self.callproc("dbms_redact.add_policy", policy)

    def drop_policy(self, policy: dict):
        self.callproc("dbms_redact.drop_policy", policy)

    def enable_policy(self, policy: dict):
        self.callproc("dbms_redact.enable_policy", policy)

    def disable_policy(self, policy: dict):
        self.callproc("dbms_redact.disable_policy", policy)

    def alter_policy(self, policy: dict):
        self.callproc("dbms_redact.alter_policy", policy)

    def create_policy_expression(self, policy_expression: dict):
        self.callproc(
            "dbms_redact.create_policy_expression", policy_expression,
        )

    def apply_policy_expr_to_col(self, payload: dict):
        self.callproc(
            "dbms_redact.apply_policy_expr_to_col",
            {**payload, "policy_expression_name": None},
        )
        self.callproc("dbms_redact.apply_policy_expr_to_col", payload)

    def update_policy_expression(self, payload: dict):
        self.callproc("dbms_redact.update_policy_expression", payload)

    def drop_policy_expression(self, payload: dict):
        self.callproc("dbms_redact.drop_policy_expression", payload)
