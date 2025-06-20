from dataclasses import dataclass
from sqlalchemy import BigInteger, String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column

from datetime import datetime
from uuid import UUID

from app.config.database_config import Base
from app.models.auditor_base import AuditorBaseModel
from sqlalchemy import TIMESTAMP, func, Uuid
from app.models.troncal import Troncal
from app.utils.jwt_util import get_authenticated_user_id

class Zone(Base):
    __tablename__ = "zone_coverage"

    zone_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="Unique identifier")
    ubigeo_department_id: Mapped[str] = mapped_column(String(100), nullable=False)
    ubigeo_province_id: Mapped[str] = mapped_column(String(100), nullable=True)
    zone_code: Mapped[str] = mapped_column(String(100), nullable=False)
    troncales: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    box_naps: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    advance_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    state_id: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    sale_id: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    # troncals = relationship(Troncal, back_populates="zone", cascade="all")

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False, onupdate=None)
    created_by: Mapped[UUID] = mapped_column(Uuid, nullable=False, default=get_authenticated_user_id, onupdate=None)
    updated_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), onupdate=func.now(), nullable=True)
    updated_by: Mapped[UUID | None] = mapped_column(Uuid, nullable=True, onupdate=get_authenticated_user_id)

@dataclass
class ZoneDTO:
    code: str
    troncales: str
