from typing import List, Optional
import app.models.schemas.metadata as ms


MASKED_COLUMNS = """
    SELECT
        s.name as schema_name,
        t.name as table_name,
        c.name column_name,
        c.is_masked,
        c.masking_function
    FROM sys.masked_columns AS c
    JOIN sys.tables AS t
    	ON  c.[object_id] = t.[object_id]
    JOIN sys.schemas s
        ON t.[schema_id] = s.[schema_id]
    WHERE is_masked = 1
"""

SCHEMAS = "SELECT s.name schema_name from sys.schemas as s"

TABLES = """
    select s.name as schema_name, t.name as table_name
    from sys.schemas AS s
    join sys.tables AS t
        on s.[schema_id] = t.[schema_id]
"""

COLUMNS = """
    select
     	s.name schema_name,
     	t.name table_name,
     	c.name column_name
     from
     	sys.columns c,
     	sys.tables 	t,
     	sys.schemas s
     where
     	s.schema_id  = t.schema_id and
     	t.object_id  = c.object_id
"""

USERS = """
    select name as username,
        create_date,
        modify_date,
        type_desc as type,
        authentication_type_desc as authentication_type
    from sys.database_principals
    where type not in ('A', 'G', 'R', 'X')
        and sid is not null
        and name != 'guest'
    order by username
"""


def users():
    return USERS


def schemas():
    return SCHEMAS


def tables(schema_name: str):
    return f"""
        select q.* from ({TABLES}) as q where q.schema_name = '{schema_name}'
    """


def columns(schema_name: str, table_name: str):
    return f"""
        select q.* from ({COLUMNS}) as q
        where q.schema_name = '{schema_name}' and q.table_name = '{table_name}'
    """


def masked_columns(
    schema_name: str, table_name: str, column_name: Optional[str] = None
):
    filters = []
    if schema_name:
        filters.append(f"s.name = '{schema_name}'")
    if table_name:
        filters.append(f"t.name = '{table_name}'")
    if column_name:
        filters.append(f"c.name = '{column_name}'")

    if len(filters) == 0:
        return MASKED_COLUMNS

    return f"{MASKED_COLUMNS} and {' and '.join(filters)}"
