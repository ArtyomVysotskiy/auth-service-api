from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import FastapiProvider

from app.adapters.config import Config, PostgresqlConfig, SecretConfig
from app.bootstrap.di.providers.adapter import AdapterProvider
from app.bootstrap.di.providers.config import ConfigProvider
from app.bootstrap.di.providers.connection import ConnectionProvider
from app.bootstrap.di.providers.gateways import GatewayProvider
from app.bootstrap.di.providers.interactors import InteractorsProvider


def get_async_container(
    config: Config,
) -> AsyncContainer:
    container = make_async_container(
        ConfigProvider(),
        FastapiProvider(),
        AdapterProvider(),
        GatewayProvider(),
        InteractorsProvider(),
        ConnectionProvider(),
        context={
            PostgresqlConfig: config.postgresql,
            SecretConfig: config.secret,
        },
    )
    return container
