from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import app.models.orm as models
import app.models.schemas.oracle.redact as s
import app.models.schemas.metadata as ms
from .base import router
from app.database import get_db
import pydash
from app.vendors.oracle import Oracle


@router.get(
    "/connections/{conn_id}/oracle/redact/policies/one",
    response_model=s.PolicyOut,
)
def get_one(
    conn_id: int,
    object_owner: str,
    object_name: str,
    policy_name: str,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    return oracle.get_policy(object_owner, object_name, policy_name)


@router.get(
    "/connections/{conn_id}/oracle/redact/policies/owners",
    response_model=List[ms.Schema],
)
def get_owners(
    conn_id: int, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    return oracle.get_policy_owners()


@router.get(
    "/connections/{conn_id}/oracle/redact/policies/owners/{owner}/tables",
    response_model=List[ms.Table],
)
def get_tables(
    conn_id: int, owner: str, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    return oracle.get_policy_tables(owner)


@router.post(
    "/connections/{conn_id}/oracle/redact/policies", response_model=bool,
)
def create(
    policy: s.PolicyCreateIn, conn_id: int, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    oracle.add_policy(policy.dict())
    return True


@router.get(
    "/connections/{conn_id}/oracle/redact/policies",
    response_model=List[s.PolicyOut],
)
def get_all(
    conn_id: int,
    object_owner: Optional[str] = None,
    object_name: Optional[str] = None,
    db: Session = Depends(get_db),
) -> List[s.PolicyOut]:
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    return oracle.get_policies(object_owner, object_name)


@router.delete(
    "/connections/{conn_id}/oracle/redact/policies", response_model=bool,
)
def delete(
    conn_id: int,
    object_schema: str,
    object_name: str,
    policy_name: str,
    db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    policy = dict(
        object_schema=object_schema,
        object_name=object_name,
        policy_name=policy_name,
    )
    oracle: Oracle = conn.get_vendor()
    oracle.drop_policy(policy)
    return True


@router.put(
    "/connections/{conn_id}/oracle/redact/policies/enable",
    response_model=bool,
)
def enable(
    policy: s.PolicyEnableIn, conn_id: int, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)

    oracle: Oracle = conn.get_vendor()
    oracle.enable_policy(policy.dict())
    return True


@router.put(
    "/connections/{conn_id}/oracle/redact/policies/disable",
    response_model=bool,
)
def disable(
    policy: s.PolicyEnableIn, conn_id: int, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    oracle.disable_policy(policy.dict())
    return True


@router.put(
    "/connections/{conn_id}/oracle/redact/policies", response_model=bool,
)
def update(
    policy: s.PolicyUpdateIn, conn_id: int, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    oracle.alter_policy(policy.dict())
    return True


@router.post(
    "/connections/{conn_id}/oracle/redact/policies/ask/tables",
    response_model=List[s.PolicyTableAnswer],
)
def ask_tables(
    tables: List[ms.Table], conn_id: int, db: Session = Depends(get_db),
):
    conn = db.query(models.Connection).get(conn_id)
    oracle: Oracle = conn.get_vendor()
    policies: List[s.PolicyOut] = oracle.get_policies_for_tables(tables)
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
