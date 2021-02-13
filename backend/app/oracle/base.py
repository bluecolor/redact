from typing import Any, Optional
import app.models.orm as models
import cx_Oracle


def connect(connection: models.Connection) -> Any:
    return cx_Oracle.connect(
        connection.username, connection.password_plain, connection.dsn
    )


def fetchall(cursor):
    columns = [col[0].lower() for col in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return rows


def queryall(connection: models.Connection, query: str) -> Any:
    with connect(connection=connection) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = fetchall(cursor=cursor)
        cursor.close()
    return result


def ping(connection: models.Connection):
    result = False
    with connect(connection) as conn:
        try:
            result = conn.ping() is None
        except:
            result = False
    return result


def callproc(
    connection: models.Connection, proc: str, params: Optional[dict] = dict()
) -> Any:
    with connect(connection) as conn:
        cursor = conn.cursor()
        print(params)
        cursor.callproc(proc, keywordParameters=params)
        cursor.close()
