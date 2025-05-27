from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    age: Mapped[int | None] = mapped_column(nullable=True)
    description: Mapped[str | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] =  mapped_column(DateTime(timezone=True), nullable=True)
