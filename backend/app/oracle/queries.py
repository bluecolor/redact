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

ALL_OBJECT_OWNERS = """
    select username as name from all_users
"""

ALL_TAB_COLS = """
    select owner, table_name, column_name, data_type from all_tab_cols
"""


def redaction_policies(
    object_owner: str = None, object_name: str = None, policy_name: str = None
) -> str:
    filters = []
    if object_owner:
        filters.append(f"object_owner = '{object_owner}'")
    if object_name:
        filters.append(f"object_name = '{object_name}'")
    if object_name:
        filters.append(f"policy_name = '{policy_name}'")

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


def redaction_expression(name: str) -> str:
    return f"{REDACTION_EXPRESSIONS} where policy_expression_name = '{name}'"


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


def all_object_owners() -> str:
    return ALL_OBJECT_OWNERS


def columns_like(schema, expression) -> str:
    return f"""
        select table_name, column_name from all_tab_cols where
        owner = '{schema}' and regexp_like(column_name, '{expression}', 'i')
    """
