from dataclasses import dataclass

from pydantic import BaseModel, Field

from app.adapters.idp import TokenUserIdProvider, UnauthorizedError
from app.application.common.uow import UoW
from app.application.gateway.user_gateway import UserGateway


class UpdateUserRequest(BaseModel):
    age: int | None = Field(ge=0, le=120, default=None, description="Новый возраст пользователя")
    description: str | None = Field(
        min_length=2, max_length=150, default=None, description="Новое описание пользователя"
    )


@dataclass(slots=True, frozen=True)
class UpdateUser:
    uow: UoW
    user_gateway: UserGateway
    user_id_provider: TokenUserIdProvider

    async def execute(self, request: UpdateUserRequest) -> None:
        user_id = await self.user_id_provider.get_user_id()
        user = await self.user_gateway.get_by_id(user_id)

        if not user:
            raise UnauthorizedError

        if request.age:
            user.age = request.age

        if request.description:
            user.description = request.description

        await self.uow.commit()
