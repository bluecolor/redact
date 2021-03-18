from celery.result import allow_join_result
from typing import List, Union
import json
from celery import group, chord
from sqlalchemy_utils import models
from sqlalchemy.orm import Session
from app.celery import celery_app
from app.database import get_db
from app.models.orm import plan_instance
from app.oracle.metadata import get_table_packs
from app.models.schemas import Table, Rule
import app.models.orm as m
from app.oracle.discovery import search_tables
from fastapi.encoders import jsonable_encoder


def update_status(p: Union[m.Plan, m.PlanInstance], status: str, db: Session):
    p.status = status
    db.add(p)
    db.commit()
    db.refresh(p)


@celery_app.task
def callback(results, conn_id, plan_id, plan_instance_id):
    print(f"Success callback: {conn_id} {plan_id} {plan_instance_id}")
    for db in get_db():

        plan = (
            db.query(m.Plan)
            .filter(m.Connection.id == conn_id, m.Plan.id == plan_id,)
            .one()
        )

        plan_instance = (
            db.query(m.PlanInstance)
            .filter(
                m.Connection.id == conn_id,
                m.Plan.id == plan_id,
                m.PlanInstance.id == plan_instance_id,
            )
            .one()
        )
        update_status(plan, "success", db)
        update_status(plan_instance, "success", db)


@celery_app.task
def on_chord_error(task_id, conn_id, plan_id, plan_instance_id):
    print(f"Error callback: {conn_id} {plan_id}, {plan_instance_id}")
    for db in get_db():
        plan = (
            db.query(m.Plan)
            .filter(m.Connection.id == conn_id, m.Plan.id == plan_id,)
            .one()
        )

        plan_instance = (
            db.query(m.PlanInstance)
            .filter(
                m.Connection.id == conn_id,
                m.Plan.id == plan_id,
                m.PlanInstance.id == plan_instance_id,
            )
            .one()
        )
        update_status(plan, "error", db)
        update_status(plan_instance, "error", db)


@celery_app.task(acks_late=True)
def start(conn_id: int, plan_instance_id: int):
    for db in get_db():
        plan_instance: m.PlanInstance = db.query(m.PlanInstance).filter(
            m.Connection.id == conn_id, m.PlanInstance.id == plan_instance_id
        ).one()
        update_status(plan_instance, "running", db)

        schemas = json.loads(plan_instance.schemas)
        connection = db.query(m.Connection).get(conn_id)
        packs: List[List[Table]] = get_table_packs(
            connection, schemas, plan_instance.worker_count
        )
        plan_id: int = plan_instance.plan_id
        cb = callback.s(conn_id, plan_id, plan_instance_id).on_error(
            on_chord_error.s(conn_id, plan_id, plan_instance_id)
        )
        chord(
            [
                run.s(
                    conn_id, plan_instance_id, json.dumps(pack, default=vars)
                )
                for pack in packs
            ]
        )(cb)


@celery_app.task(acks_late=True)
def run(
    conn_id: int, plan_instance_id: int, tables_json: str,
):
    for db in get_db():
        connection = db.query(m.Connection).get(conn_id)
        plan_instance = (
            db.query(m.PlanInstance)
            .filter(
                m.Connection.id == conn_id,
                m.PlanInstance.id == plan_instance_id,
            )
            .one()
        )
        tables = [Table.parse_obj(t) for t in json.loads(tables_json)]
        for result in search_tables(
            connection=connection,
            tables=tables,
            rules=[Rule.from_orm(r) for r in plan_instance.plan.rules],
        ):
            if result.hit:
                d = result.discovery
                discovery = m.Discovery(
                    schema_name=d.schema_name,
                    table_name=d.table_name,
                    column_name=d.column_name,
                    plan_instance_id=plan_instance_id,
                    rule_id=result.discovery.rule.id,
                )
                db.add(discovery)
                db.commit()
