from sqlalchemy import BigInteger, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.models.auditor_base import AuditorBaseModel


class Feature(AuditorBaseModel):
    __tablename__ = "features"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="Unique identifier")
    name: Mapped[str] = mapped_column(String(100), nullable=False, comment="Feature name")
    description: Mapped[str | None] = mapped_column(String(500), nullable=True, comment="Feature description")
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, comment="Marks record as active or deleted")