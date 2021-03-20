import json
import tempfile
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
from app.models.orm.category import Category
import app.models.schemas as s
from app.models.schemas.redact import CategoryExportOut
from .base import router
from app.database import get_db
from app.oracle import redact
from fastapi.responses import FileResponse
import pydash


@router.post("/connections/{conn_id}/settings/export")
def export(conn_id: int, payload: s.ExportIn, db: Session = Depends(get_db)):
    conn = db.query(models.Connection).get(conn_id)
    result = {}
    if "expressions" in payload.options:
        result["expressions"] = [
            e.dict() for e in redact.get_expressions(connection=conn)
        ]
    if "policies" in payload.options:
        policies = redact.get_policies(connection=conn)
        columns = redact.get_columns(connection=conn)
        result["policies"] = []
        for p in policies:
            policy = p.dict()
            policy["columns"] = [
                c.dict()
                for c in pydash.filter_(
                    columns,
                    lambda x: x.object_owner == p.object_owner
                    and x.object_name == p.object_name,
                )
            ]
            result["policies"].append(policy)
    if "categories" in payload.options:
        result["categories"] = [
            CategoryExportOut.from_orm(c).dict()
            for c in db.query(models.Category)
            .filter(models.Connection.id == conn_id)
            .all()
        ]

    with tempfile.NamedTemporaryFile(
        prefix=conn.name, suffix="_export.json", mode="w", delete=False
    ) as handler:
        handler.write(json.dumps(result, indent=4))
        name = handler.name

    return FileResponse(name)
