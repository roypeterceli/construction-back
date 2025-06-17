from sqlalchemy import CheckConstraint, BigInteger, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models.auditor_base import AuditorBaseModel


class Nap(AuditorBaseModel):
    __tablename__ = "naps"

    nap_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="Unique identifier")
    node_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="Node identifier")
    id_ports: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="Ports identifier")
    nap_state: Mapped[int] = mapped_column(BigInteger, nullable=False, default=True, comment="")
    nap_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, comment="")

    __table_args__ = (
        CheckConstraint('id_ports > 0', name='check_id_ports'),
    )

    node = relationship("Nodo", back_populates="cajas_nap")
    ports = relationship("Puerto", back_populates="nap", cascade="all, delete")