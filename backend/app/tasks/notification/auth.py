import json
from app.models.orm import User
from .base import notify
from app.models.schemas.notification import Notification, LOGIN, LOGOUT


def notify_login(user: User):
    data = {"name": user.name, "email": user.email, "id": user.id}
    n = Notification(type=LOGIN, text="Peer login", data=data)
    notify.delay(json.dumps(n.dict()))
