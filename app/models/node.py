from sqlalchemy import BigInteger, Boolean, String, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models.auditor_base import AuditorBaseModel


class Node(AuditorBaseModel):
    __tablename__ = "nodes"

    node_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="Unique identifier")
    node_correlative: Mapped[str] = mapped_column(String(100), nullable=False, comment="")
    node_sufix: Mapped[str] = mapped_column(String(250), nullable=True, comment="")
    naps_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment="Count of naps")
    node_state: Mapped[int] = mapped_column(BigInteger, nullable=False, comment="")
    sale_sate: Mapped[int] = mapped_column(BigInteger, nullable=False, comment="")
    troncal_id: Mapped[int] = mapped_column(BigInteger, nullable=False, comment="")
    node_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, comment="Flag to enable or disable flow")

    troncal = relationship("Troncal", back_populates="nodos")
    box_nap = relationship("CajaNAP", back_populates="nodo", cascade="all, delete")
