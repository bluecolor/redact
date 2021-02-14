import app.models.orm as model
from app.models.schemas.user import User, UserCreateIn
from .base import router


@router.post("/users", tags=["Users"], response_model=User)
async def create_user(request: UserCreateIn):
    new_user: model.User = await model.User.create(**request.dict())
    return User.from_orm(new_user)
