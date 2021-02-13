REDACTION_POLICIES = """
    select * from redaction_policies
"""

REDACTION_EXPRESSIONS = """
    select * from redaction_expressions
"""

REDACTION_COLUMNS = """
    select * from redaction_columns
"""

ALL_TABLES = """
    select owner, table_name from all_tables
"""

ALL_TAB_COLS = """
    select owner, table_name, column_name, data_type from all_tab_cols
"""


def redaction_policies(owner: str = None, table_name: str = None) -> str:
    filters = []
    if owner:
        filters.append(f"owner = '{owner}'")
    if table_name:
        filters.append(f"table_name = '{table_name}'")

    if len(filters) == 0:
        return REDACTION_POLICIES

    return f"{REDACTION_POLICIES} where {' and '.join(filters)}"


def redaction_expressions(object_owner: str = None, object_name: str = None):
    filters = []
    if object_owner:
        filters.append(f"object_owner = '{object_owner}'")
    if object_name:
        filters.append(f"object_name = '{object_name}'")
    if len(filters) == 0:
        return REDACTION_EXPRESSIONS

    return f"{REDACTION_EXPRESSIONS} where {' and '.join(filters)}"


def redaction_columns(
    object_owner: str = None, object_name: str = None
) -> str:
    filters = []
    if object_owner:
        filters.append(f"object_owner = '{object_owner}'")
    if object_name:
        filters.append(f"object_name = '{object_name}'")
    if len(filters) == 0:
        return REDACTION_COLUMNS

    return f"{REDACTION_COLUMNS} where {' and '.join(filters)}"


def all_tables(owner: str = None) -> str:
    if not owner:
        return ALL_TABLES

    return f"{ALL_TABLES} where owner = '{owner}'"


def all_tab_cols(owner: str = None, table_name: str = None):
    filters = []
    if owner:
        filters.append(f"owner = '{owner}'")
    if table_name:
        filters.append(f"table_name = '{table_name}'")

    if len(filters) == 0:
        return ALL_TAB_COLS

    return f"{ALL_TAB_COLS} where {' and '.join(filters)}"
