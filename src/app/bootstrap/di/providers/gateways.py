from dishka import Provider, Scope, WithParents, provide_all

from app.adapters.gateway.access_token import AccessTokenGatewayImpl
from app.adapters.gateway.user import UserGatewayImpl


class GatewayProvider(Provider):
    scope = Scope.REQUEST

    provides = provide_all(
        WithParents[AccessTokenGatewayImpl],  # type: ignore[misc]
        WithParents[UserGatewayImpl],  # type: ignore[misc]
    )
