from uuid import UUID

from adaptix.conversion import get_converter
from pydantic import BaseModel, Field

from app.models.user import User


class UserData(BaseModel):
    id: UUID = Field(description="Идентификатор пользователя")
    name: str = Field(description="Имя пользователя")
    age: int | None = Field(default=None, description="Возраст пользователя")
    description: str | None = Field(default=None, description="Описание пользователя")

convert_user_model_to_dto = get_converter(User, UserData)
