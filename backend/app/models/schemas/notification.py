from typing import Any, Optional
from pydantic import BaseModel, ValidationError, validator


PLAN_INSTANCE_START = "plan_instance_start"
PLAN_INSTANCE_ERROR = "plan_instance_error"
PLAN_INSTANCE_SUCCESS = "plan_instance_success"
PLAN_INSTANCE_DONE = "plan_instance_done"
LOGIN = "login"
LOGOUT = "logout"

notification_types = [
    PLAN_INSTANCE_START,
    PLAN_INSTANCE_ERROR,
    PLAN_INSTANCE_SUCCESS,
    PLAN_INSTANCE_DONE,
    LOGIN,
    LOGOUT,
]


class Notification(BaseModel):
    type: str
    text: Optional[str]
    data: Optional[Any]
    time: Optional[str]
    critical: Optional[bool] = False

    @validator("type")
    def type_mustbe_registered(cls, v):
        if v not in notification_types:
            raise ValueError(f"{v} is not a valid notification type")
        return v
