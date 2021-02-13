from typing import Any
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


def ping(connection: models.Connection):
    result = False
    with connect(connection) as conn:
        try:
            result = conn.ping() is None
        except:
            result = False
    return result
