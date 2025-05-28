from dishka import Provider, Scope, from_context, provide

from app.adapters.config import PostgresqlConfig, SecretConfig


class ConfigProvider(Provider):
    scope = Scope.APP

    configs = (
        from_context(PostgresqlConfig)
        + from_context(SecretConfig)
    )