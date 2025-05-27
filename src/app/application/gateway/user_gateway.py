from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from app.models.user import User

class UserGateway(Protocol):
    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> User | None: ...

    @abstractmethod
    async def get_by_name(self, name: str) -> User | None: ...
