import json
from asyncio import sleep
from typing import Union
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
import app.models.orm as models
from arq.connections import ArqRedis, RedisSettings, create_pool
from app.models.orm import PlanInstance, Plan, Rule
from app.oracle.discovery import search


def update_status(
    p: Union[models.Plan, models.PlanInstance], status: str, db: Session
):
    p.status = status
    db.add(p)
    db.commit()
    db.refresh(p)


async def run_plan(ctx: dict, conn_id: int, plan_id: int):
    # redis: ArqRedis = await create_pool(settings)

    for db in ctx["db"]:
        plan: Plan = db.query(models.Plan).get(plan_id)
        plan_instance: models.PlanInstance = plan.get_new_instance()
        update_status(plan_instance, "running", db)

        for rule in plan_instance.plan.rules:  # type: Rule
            print(f"Checking rule {rule.name}")
            for discovery in search(
                plan_instance.plan.connection, plan_instance.schema_list, rule
            ):
                print("found discovery....")
                discovery.plan_instance_id = plan_instance.id
                db.add(discovery)
                db.commit()

        update_status(plan_instance, "success", db)
        update_status(plan, "success", db)

    # redis.publish_json("plan:run", {"hello":"world"})
    # await sleep(20)
