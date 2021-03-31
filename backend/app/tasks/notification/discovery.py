import json
from app.models.orm import PlanInstance
from .base import notify
from app.models.schemas.notification import (
    Notification,
    PLAN_INSTANCE_DONE,
    PLAN_INSTANCE_START,
    PLAN_INSTANCE_ERROR,
    PLAN_INSTANCE_SUCCESS,
)
from fastapi.encoders import jsonable_encoder


def notify_plan_instance_start(plan_instance: PlanInstance):
    data = jsonable_encoder(plan_instance)
    n = Notification(
        type=PLAN_INSTANCE_START, text="Plan run started", data=data
    )
    notify.delay(json.dumps(n.dict()))


def notify_plan_instance_error(plan_instance: PlanInstance):
    data = jsonable_encoder(plan_instance)
    n = Notification(
        type=PLAN_INSTANCE_ERROR, text="Plan run error", data=data
    )
    notify.delay(json.dumps(n.dict()))


def notify_plan_instance_success(plan_instance: PlanInstance):
    data = jsonable_encoder(plan_instance)
    n = Notification(
        type=PLAN_INSTANCE_SUCCESS, text="Plan run completed", data=data,
    )
    notify.delay(json.dumps(n.dict()))
