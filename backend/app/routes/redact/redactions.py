from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.redact as s
import app.models.schemas.metadata as ms
from .base import router
from app.database import get_db
from app.oracle import redact
import pydash


@router.post(
    "/connections/{conn_id}/redact/ask/columns",
    response_model=List[s.ColumnAnswerOut],
)
def ask_columns(
    conn_id: int, columns: List[ms.ColumnIn], db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    expressions = redact.get_expressions_in_columns(connection, columns)
    columns = redact.get_columns_in_columns(connection, columns)
    answers: List[s.ColumnAnswerOut] = []

    for c in columns:
        answer: s.ColumnAnswerOut = s.ColumnAnswerOut(
            owner=c.owner, table_name=c.table_name, column_name=c.column_name
        )
        answer.column = pydash.find(
            columns,
            lambda x: x.object_owner == c.owner
            and x.object_name == c.table_name
            and x.column_name == c.column_name,
        )
        answer.expression = pydash.find(
            expressions,
            lambda x: x.object_owner == c.owner
            and x.object_name == c.table_name
            and x.column_name == c.column_name,
        )
        answers.append(answer)

    return answers
