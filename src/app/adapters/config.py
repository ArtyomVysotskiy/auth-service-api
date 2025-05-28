import os
from dataclasses import dataclass

from typing_extensions import Self


@dataclass(frozen=True, slots=True)
class ServerConfig:
    host: str
    port: int
    access_log: bool


@dataclass(frozen=True, slots=True)
class SecretConfig:
    secret_key: str


@dataclass(frozen=True, slots=True)
class PostgresqlConfig:
    username: str
    password: str
    host: str
    port: int
    database: str

    @property
    def connection_url(self) -> str:
        return f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}/{self.database}"


@dataclass(frozen=True, slots=True)
class Config:
    server: ServerConfig
    postgresql: PostgresqlConfig
    secret: SecretConfig

    @classmethod
    def load_from_environment(cls) -> Self:
        return cls(
            server=ServerConfig(
                host=os.environ["SERVER_HOST"],
                port=int(os.environ["SERVER_PORT"]),
                access_log=bool(int(os.environ["SERVER_ACCESS_LOG"])),
            ),
            postgresql=PostgresqlConfig(
                username=os.environ["POSTGRES_USERNAME"],
                password=os.environ["POSTGRES_PASSWORD"],
                host=os.environ["POSTGRES_HOST"],
                port=int(os.environ["POSTGRES_PORT"]),
                database=os.environ["POSTGRES_DATABASE"],
            ),
            secret=SecretConfig(
                secret_key=os.environ["SECRET_KEY"],
            ),
        )
