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

TABLES_AND_COLUMNS = """
    select
        'column' type,
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
    union
    select
        'table' type,
     	s.name schema_name,
     	t.name table_name,
     	null column_name
     from
     	sys.tables 	t,
     	sys.schemas s
     where
     	s.schema_id  = t.schema_id
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


def tables_and_columns_in_schemas(search_str, schemas):
    query = f"""
        select q.* from ({TABLES_AND_COLUMNS}) as q
        where
            lower(concat(q.schema_name, '.', q.table_name, '.', q.column_name)) like lower('%{search_str}%') or
            lower(concat(q.schema_name, '.', q.table_name)) like lower('%{search_str}%') or
            lower(concat(q.table_name, '.', q.column_name)) like lower('%{search_str}%')
    """

    if len(schemas) > 0:
        filters = ", ".join([f"'{s}'" for s in schemas])
        return f"""select s.* from ({query}) as s where schema_name in ({filters})"""

    return query


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


def sample(schema_name: str, table_name: str, column_name: str) -> str:
    return f"""select q.{column_name} from (
        select {column_name} from {schema_name}.{table_name}
        ) q
        order by 1 offset 0 rows fetch next 10 rows only
    """


def tables_in_schemas(schemas: List[str]) -> str:
    return f"""select q.* from ({TABLES}) as q where q.schema_name in ({', '.join(["'"+s+"'" for s in schemas]) })"""


def columns_like(*, schema, table_name=None, expression) -> str:
    if table_name is None:
        return f"""
            select q.* from ({COLUMNS}) q where q.schema_name = '{schema}' and
            patindex('%' + q.column_name +'%','{expression}')  !=0
        """

    return f"""
        select q.* from ({COLUMNS}) q where q.schema_name = '{schema}' and
        q.table_name = '{table_name}' and
        patindex('%' + q.column_name +'%','{expression}')  !=0
    """
