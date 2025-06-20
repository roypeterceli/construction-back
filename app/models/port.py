from sqlalchemy import ForeignKey, UniqueConstraint, BigInteger, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models.auditor_base import AuditorBaseModel


class Ports(AuditorBaseModel):
    __tablename__ = "ports"

    port_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="Unique identifier")
    nap_id: Mapped[str] = mapped_column(String(100), ForeignKey('naps.nap_id'), nullable=False, comment="")
    port: Mapped[str] = mapped_column(String(250), nullable=True, comment="")
    port_active: Mapped[str] = mapped_column(String(250), nullable=False, comment="")

    # nap = relationship("Nap", back_populates="ports")

    # __table_args__ = (UniqueConstraint('numero', 'nap_id', name='uq_numero_nap'),)

