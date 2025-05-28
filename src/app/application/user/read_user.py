from dataclasses import dataclass
from uuid import UUID

from app.adapters.idp import TokenUserIdProvider, UnauthorizedError
from app.application.data_model.user import UserData, convert_user_model_to_dto
from app.application.gateway.user_gateway import UserGateway


@dataclass(slots=True, frozen=True)
class ReadUser:
    user_gateway: UserGateway
    idp: TokenUserIdProvider

    async def execute(self) -> UserData:
        user = await self.user_gateway.get_by_id(await self.idp.get_user_id())
        if not user:
            raise UnauthorizedError

        return convert_user_model_to_dto(user)
