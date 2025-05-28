from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.gateway.user_gateway import UserGateway
from app.models.user import User


class UserGatewayImpl(UserGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, user_id: UUID) -> User | None:
        q = select(User).where(User.id == user_id)
        res = await self._session.execute(q)
        return res.scalar()

    async def get_by_name(self, name: str) -> User | None:
        q = select(User).where(User.name == name)
        res = await self._session.execute(q)
        return res.scalar()
