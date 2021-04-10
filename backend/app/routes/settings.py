import json
import tempfile
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas as s
from app.models.schemas.discovery import PlanOut, RuleOut
from .base import router
from app.database import get_db
from fastapi.responses import FileResponse
import pydash
from fastapi.encoders import jsonable_encoder
from fastapi import File, UploadFile


@router.post("/connections/{conn_id}/settings/export")
def export_settings(
    conn_id: int, payload: s.ExportIn, db: Session = Depends(get_db)
):
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
            CategoryOut.from_orm(c).dict()
            for c in db.query(models.Category)
            .filter(models.Connection.id == conn_id)
            .all()
        ]
    if "plans" in payload.options:
        result["plans"] = [
            PlanOut.from_orm(p).dict()
            for p in db.query(models.Plan)
            .filter(models.Connection.id == conn_id)
            .all()
        ]
    if "rules" in payload.options:
        result["rules"] = [
            RuleOut.from_orm(r).dict()
            for r in db.query(models.Rule)
            .filter(models.Connection.id == conn_id)
            .all()
        ]

    with tempfile.NamedTemporaryFile(
        prefix=conn.name, suffix="_export.json", mode="w", delete=False
    ) as handler:
        handler.write(json.dumps(jsonable_encoder(result), indent=4))
        name = handler.name

    return FileResponse(name)


@router.post("/connections/{conn_id}/settings/import")
async def import_settings(
    conn_id: int,
    ignore_errors: bool,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    content = json.loads(await file.read())

    result: dict = {}

    if "expressions" in content:
        result["expressions"] = []
        for e in content["expressions"]:
            try:
                redact.create_policy_expression(conn, e)
                result["expressions"].append(e)
            except:
                ...
    if "policies" in content:
        ...

    return result
