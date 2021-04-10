from typing import List, Optional
import app.models.schemas.metadata as ms


REDACTION_POLICIES = """
    select * from redaction_policies
"""

REDACTION_POLICY_OWNERS = """
    select distinct object_owner as name from redaction_policies
"""

REDACTION_POLICY_TABLES = """
    select distinct object_owner as owner, object_name as table_name from redaction_policies
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

ALL_SCHEMAS = """
    select username as name from all_users
"""


ALL_TAB_COLS = """
    select owner, table_name, column_name, data_type from all_tab_cols
"""

ALL_TABS_AND_COLS = """
    select 'column' type, owner schema_name, table_name, column_name from all_tab_cols
    union all
    select 'table' type, owner schema_name, table_name, null column_name from all_tables
"""


def tables(schema_name: Optional[str] = None) -> str:
    if not schema_name:
        return ALL_TABLES

    return f"{ALL_TABLES} where owner = '{schema_name}'"


def schemas() -> str:
    return ALL_SCHEMAS


def columns(schema_name: str = Optional[None], table_name: str = None):
    filters = []
    if schema_name:
        filters.append(f"owner = '{schema_name}'")
    if table_name:
        filters.append(f"table_name = '{table_name}'")

    if len(filters) == 0:
        return ALL_TAB_COLS

    return f"{ALL_TAB_COLS} where {' and '.join(filters)}"


def tables_in_schemas(schemas: List[str]) -> str:
    return f"""{ALL_TABLES} where owner in ({', '.join(["'"+s+"'" for s in schemas]) })"""


def tables_and_columns_in_schemas(q: str, schemas: List[str] = []) -> str:
    query = f"""
        select *
        from ({ALL_TABS_AND_COLS}) s
        where (upper(s.schema_name||s.table_name||s.column_name) like '%{q.upper()}%') or
              (upper(s.schema_name||'.'||s.table_name||'.'||s.column_name) like '%{q.upper()}%')
    """

    if len(schemas) > 0:
        filters = ", ".join([f"'{s}'" for s in schemas])
        return f"""select * from ({query}) where owner in ({filters})"""

    return query


def sample(schema_name: str, table_name: str, column_name: str) -> str:
    return f"""select {column_name} from (
        select {column_name} from {schema_name}.{table_name} order by dbms_random.random)
        where rownum < 10"""


def redaction_policy_owners() -> str:
    return REDACTION_POLICY_OWNERS


def redaction_policy_tables(owner: str) -> str:
    return f"{REDACTION_POLICY_TABLES} where object_owner='{owner}'"


def redaction_policies(
    object_owner: str = None, object_name: str = None, policy_name: str = None
) -> str:
    filters = []
    if object_owner:
        filters.append(f"object_owner = '{object_owner}'")
    if object_name:
        filters.append(f"object_name = '{object_name}'")
    if policy_name:
        filters.append(f"policy_name = '{policy_name}'")

    if len(filters) == 0:
        return REDACTION_POLICIES

    return f"{REDACTION_POLICIES} where {' and '.join(filters)}"


def redaction_policies_for_tables(tables: List[ms.Table]) -> str:
    filters = [
        f"(object_owner = '{t.owner}' and object_name = '{t.table_name}')"
        for t in tables
    ]
    return f"{REDACTION_POLICIES} where {' or '.join(filters)}"


def redaction_expressions(
    object_owner: str = None, object_name: str = None, column_name: str = None
):
    filters = []
    if object_owner:
        filters.append(f"object_owner = '{object_owner}'")
    if object_name:
        filters.append(f"object_name = '{object_name}'")
    if column_name:
        filters.append(f"column_name = '{column_name}'")
    if len(filters) == 0:
        return REDACTION_EXPRESSIONS

    return f"{REDACTION_EXPRESSIONS} where {' and '.join(filters)}"


def redaction_expressions_in_columns(columns: List[ms.ColumnIn]) -> str:
    filters = [
        f"(object_owner = '{c.owner}' and object_name='{c.table_name}' and column_name='{c.column_name}')"
        for c in columns
    ]
    return f"{REDACTION_EXPRESSIONS} where {' and '.join(filters)}"


def redaction_columns_in_columns(columns: List[ms.ColumnIn]) -> str:
    filters = [
        f"(object_owner = '{c.owner}' and object_name='{c.table_name}' and column_name='{c.column_name}')"
        for c in columns
    ]
    return f"{REDACTION_COLUMNS} where {' and '.join(filters)}"


def redaction_expression(name: str) -> str:
    return f"{REDACTION_EXPRESSIONS} where policy_expression_name = '{name}'"


def redaction_columns(
    object_owner: str = None, object_name: str = None, column_name: str = None
) -> str:
    filters = []
    if object_owner:
        filters.append(f"object_owner = '{object_owner}'")
    if object_name:
        filters.append(f"object_name = '{object_name}'")
    if column_name:
        filters.append(f"object_name = '{column_name}'")
    if len(filters) == 0:
        return REDACTION_COLUMNS

    return f"{REDACTION_COLUMNS} where {' and '.join(filters)}"


def columns_like(*, schema, table_name=None, expression) -> str:
    if table_name is None:
        return f"""
            select table_name, column_name from all_tab_cols where
            owner = '{schema}' and regexp_like(column_name, '{expression}', 'i')
        """

    return f"""
        select table_name, column_name from all_tab_cols where
        owner = '{schema}' and table_name = '{table_name}' and regexp_like(column_name, '{expression}', 'i')
    """

