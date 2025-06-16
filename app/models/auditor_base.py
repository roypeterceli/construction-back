from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import mapped_column, Mapped

from app.config.database_config import Base
from sqlalchemy import TIMESTAMP, func, Uuid

from app.utils.jwt_util import get_authenticated_user_id


class AuditorBaseModel(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False, onupdate=None)
    created_by: Mapped[UUID] = mapped_column(Uuid, nullable=False, default=get_authenticated_user_id, onupdate=None)
    updated_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), onupdate=func.now(), nullable=True)
    updated_by: Mapped[UUID | None] = mapped_column(Uuid, nullable=True, onupdate=get_authenticated_user_id)
