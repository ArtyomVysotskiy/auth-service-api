from dishka import Provider, Scope, from_context, provide
from fastapi import Request

from app.adapters.idp import TokenBearerParser, TokenUserIdProvider
from app.adapters.token_encoder import TokenEncoder


class AdapterProvider(Provider):
    encoder = provide(TokenEncoder, scope=Scope.APP)
    request = from_context(Request, scope=Scope.REQUEST)
    token_bearer_parser = provide(TokenBearerParser, scope=Scope.REQUEST)
    idp = provide(TokenUserIdProvider, scope=Scope.REQUEST)
