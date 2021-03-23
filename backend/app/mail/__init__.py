import json
from typing import List
from starlette.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.models.orm import User, Setting
from sqlalchemy.orm.session import Session
from app.settings.mail import (
    MAIL_HOST,
    MAIL_PORT,
    MAIL_PASSWORD,
    MAIL_USERNAME,
    MAIL_FROM,
)

conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_FROM=MAIL_FROM,
    MAIL_PORT=MAIL_PORT,
    MAIL_SERVER=MAIL_HOST,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
)
fm = FastMail(conf)


class EmailSchema(BaseModel):
    email: List[EmailStr]


async def send_event_mail(event: str, sub_event: str, user: User, db: Session):

    try:
        setting: Setting = db.query(Setting.name == f"events.{event}").one()
        value: dict = json.loads(setting.value)
        if sub_event in value.events and len(value.users) > 0:
            users: List[User] = db.query(User.id.in_(value.users)).all()
            if len(users) > 0:
                emails = [u.email for u in users]
                html: str = f"""
                    <p>{user.name} modified redactions</p>
                """
                message = MessageSchema(
                    subject=f"Duck Event {event}",
                    recipients=emails,
                    body=html,
                    subtype="html",
                )
                await fm.send_message(message)
    except:
        ...

