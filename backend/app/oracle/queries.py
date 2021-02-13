REDACTION_POLICIES = """
    select * from redaction_policies
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
