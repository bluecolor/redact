from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.oracle.redact as s
import app.models.schemas.metadata as ms
from .base import router
from app.database import get_db
from app.vendor.oracle import redact
import pydash


@router.get(
    "/connections/{conn_id}/redact/policies/one", response_model=s.PolicyOut,
)
def get_one(
    conn_id: int,
    object_owner: str,
    object_name: str,
    policy_name: str,
    db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    return redact.get_policy(
        connection, object_owner, object_name, policy_name
    )


@router.get(
    "/connections/{conn_id}/redact/policies/owners",
    response_model=List[ms.ObjectOwner],
)
def get_owners(
    conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    return redact.get_policy_owners(connection)


@router.get(
    "/connections/{conn_id}/redact/policies/owners/{owner}/tables",
    response_model=List[ms.Table],
)
def get_tables(
    conn_id: int, owner: str, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    return redact.get_policy_tables(connection, owner)


@router.post(
    "/connections/{conn_id}/redact/policies", response_model=bool,
)
def create(
    policy: s.PolicyCreateIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.add_policy(connection, policy.dict())
    return True


@router.get(
    "/connections/{conn_id}/redact/policies", response_model=List[s.PolicyOut],
)
def get_all(
    conn_id: int,
    object_owner: Optional[str] = None,
    object_name: Optional[str] = None,
    db: Session = Depends(get_db),
) -> List[s.PolicyOut]:
    connection = db.query(models.Connection).get(conn_id)
    return redact.get_policies(connection, object_owner, object_name)


@router.delete(
    "/connections/{conn_id}/redact/policies", response_model=bool,
)
def delete(
    conn_id: int,
    object_schema: str,
    object_name: str,
    policy_name: str,
    db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    policy = dict(
        object_schema=object_schema,
        object_name=object_name,
        policy_name=policy_name,
    )
    redact.drop_policy(connection, policy)
    return True


@router.put(
    "/connections/{conn_id}/redact/policies/enable", response_model=bool,
)
def enable(
    policy: s.PolicyEnableIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.enable_policy(connection, policy.dict())
    return True


@router.put(
    "/connections/{conn_id}/redact/policies/disable", response_model=bool,
)
def disable(
    policy: s.PolicyEnableIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.disable_policy(connection, policy.dict())
    return True


@router.put(
    "/connections/{conn_id}/redact/policies", response_model=bool,
)
def update(
    policy: s.PolicyUpdateIn, conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    redact.alter_policy(connection, policy.dict())
    return True


@router.post(
    "/connections/{conn_id}/redact/policies/ask/tables",
    response_model=List[s.PolicyTableAnswer],
)
def ask_tables(
    tables: List[ms.Table], conn_id: int, db: Session = Depends(get_db),
):
    connection = db.query(models.Connection).get(conn_id)
    policies: List[s.PolicyOut] = redact.get_policies_for_tables(
        connection, tables
    )
    answers: List[s.PolicyTableAnswer] = []
    for t in tables:
        answer = s.PolicyTableAnswer(table=t)
        answer.policy = pydash.find(
            policies,
            lambda x: x.object_owner == t.owner
            and x.object_name == t.table_name,
        )
        answers.append(answer)

    return answers
