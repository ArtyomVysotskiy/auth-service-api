from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field

from app.adapters.token_encoder import TokenEncoder
from app.application.common.uow import UoW
from app.application.data_model.token_data import TokenResponse
from app.application.gateway.token_gateway import AccessTokenGateway
from app.application.gateway.user_gateway import UserGateway
from app.models.user import User


class SignUpUserRequest(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="Имя пользователя")
    age: int | None = Field(ge=0, le=120, default=None, description="Возраст пользователя")
    description: str | None = Field(min_length=2, max_length=150, default=None, description="Описание пользователя")


@dataclass(slots=True, frozen=True)
class SignUpUser:
    uow: UoW
    encryptor: TokenEncoder
    access_token_gateway: AccessTokenGateway
    user_gateway: UserGateway

    async def execute(self, request: SignUpUserRequest) -> TokenResponse:
        user_id = uuid4()
        user = User(
            id=user_id,
            name=request.name,
            age=request.age,
            description=request.description,
            created_at=datetime.now(tz=timezone.utc),
        )
        self.uow.add(user)

        encoded_access_token = self.encryptor.encrypt(user_id)
        await self.uow.commit()

        return TokenResponse(access_token=encoded_access_token, id=user_id)
