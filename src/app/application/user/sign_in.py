from dataclasses import dataclass

from pydantic import BaseModel, Field

from app.adapters.idp import UnauthorizedError
from app.adapters.token_encoder import TokenEncoder
from app.application.common.uow import UoW
from app.application.data_model.token_data import TokenResponse
from app.application.gateway.user_gateway import UserGateway
from app.application.gateway.token_gateway import AccessTokenGateway


class SignInUserRequest(BaseModel):
    name: str = Field(min_length=2, max_length=120, description="Имя пользователя")


@dataclass(frozen=True, slots=True)
class SignInUser:
    uow: UoW
    encryptor: TokenEncoder
    access_token_gateway: AccessTokenGateway
    user_gateway: UserGateway

    async def execute(self, request: SignInUserRequest) -> TokenResponse:
        user = await self.user_gateway.get_by_name(request.name)
        if not user:
            raise UnauthorizedError

        encoded_access_token = self.encryptor.encrypt(user.id)
        await self.uow.commit()

        return TokenResponse(access_token=encoded_access_token, id=user.id)
