from typing import List, Optional

import pkg_resources
from fastapi import Depends
from pydantic.tools import parse_obj_as
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from app.database import get_db
from app.models.orm import Setting
from app.models.schemas import SettingIn, SettingOut, VersionOut

from .base import router


@router.put("/settings/{name}", response_model=SettingOut)
def upsert(name: str, payload: SettingIn, db: Session = Depends(get_db)):
    try:
        setting: Setting = db.query(Setting).filter(Setting.name == name).one()
        setting.value = payload.value
        if payload.description is not None:
            setting.description = payload.description
    except NoResultFound:
        setting = Setting(**payload.dict())

    db.add(setting)
    db.commit()
    db.refresh(setting)
    return SettingOut.from_orm(setting)


@router.post("/settings", response_model=bool)
def upsert_all(payload: List[SettingIn], db: Session = Depends(get_db)):

    for s in payload:
        try:
            name: str = s.name
            setting: Setting = db.query(Setting).filter(
                Setting.name == name
            ).one()
            setting.value = s.value
            if s.description is not None:
                setting.description = s.description
        except NoResultFound:
            setting = Setting(**s.dict())

        db.add(setting)

    db.commit()
    return True


@router.get("/settings/version")
def get_version():
    version = pkg_resources.get_distribution("app").version
    return version


@router.get("/settings/{name}", response_model=SettingOut)
def get_seting(name: str, db: Session = Depends(get_db)):
    try:
        setting = db.query(Setting).filter(Setting.name == name).one()
        return SettingOut.from_orm(setting)
    except NoResultFound:
        return Setting()


@router.get("/settings", response_model=List[SettingOut])
def get_setings(db: Session = Depends(get_db)):
    settings = db.query(Setting).all()
    return parse_obj_as(List[SettingOut], settings)

