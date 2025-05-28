from uuid import UUID

from pydantic import BaseModel, Field


class TokenResponse(BaseModel):
    id: UUID = Field(description="Идентификатор сущности")
    access_token: str = Field(description="Токен доступа")
