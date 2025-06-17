from sqlalchemy import BigInteger, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models.auditor_base import AuditorBaseModel


class Troncal(AuditorBaseModel):
    __tablename__ = "troncals"

    troncal_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="Unique identifier")
    ubigeo_district_id: Mapped[int] = mapped_column(BigInteger, nullable=True, comment="Ubigeo district identifier")
    troncal_code: Mapped[str] = mapped_column(String(100), nullable=False, comment="Code of troncal")
    node_prefix: Mapped[str] = mapped_column(String(250), nullable=False, comment="Prefix of node")
    node_start: Mapped[int] = mapped_column(BigInteger, nullable=False, comment="")
    node_end: Mapped[int] = mapped_column(BigInteger, nullable=False, comment="")
    zone_id: Mapped[int] = mapped_column(BigInteger, nullable=False, comment="")
    troncal_state: Mapped[int] = mapped_column(BigInteger, nullable=False, default=True, comment="")
    sale_id: Mapped[int] = mapped_column(BigInteger, nullable=False, comment="")

    zone = relationship("Zona", back_populates="troncales")
    nodes = relationship("Nodo", back_populates="troncal", cascade="all, delete")