from sqlalchemy.ext.asyncio import AsyncSession

from app.application.gateway.token_gateway import AccessTokenGateway


class AccessTokenGatewayImpl(AccessTokenGateway):
    def __init__(self, session: AsyncSession):
        self._session = session
