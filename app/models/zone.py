from dataclasses import dataclass
from sqlalchemy import BigInteger, String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models.auditor_base import AuditorBaseModel


class Zone(AuditorBaseModel):
    __tablename__ = "zone_coverage"

    zone_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="Unique identifier")
    ubigeo_department_id: Mapped[str] = mapped_column(String(100), nullable=False, comment="")
    ubigeo_province_id: Mapped[str] = mapped_column(String(250), nullable=True, comment="")
    zone_code: Mapped[int] = mapped_column(Integer, nullable=False, comment="")
    troncales: Mapped[int] = mapped_column(Integer, nullable=False, comment="")
    box_naps: Mapped[int] = mapped_column(Integer, nullable=False, comment="")
    advance_id: Mapped[int] = mapped_column(Integer, nullable=False, comment="")
    state_id: Mapped[int] = mapped_column(Integer, nullable=False, comment="")
    sale_id: Mapped[int] = mapped_column(Integer, nullable=False, comment="")

    # troncales = relationship("Troncal", back_populates="zona", cascade="all, delete")

@dataclass
class ZoneDTO:
    code: str
    troncales: str
