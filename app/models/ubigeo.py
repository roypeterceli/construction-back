from dataclasses import dataclass
from sqlalchemy import String, Text
from sqlalchemy.orm import mapped_column, Mapped
from app.config.database_config import Base
# from app.models.auditor_base import AuditorBaseModel


@dataclass
class Ubigeo(Base):
    __tablename__ = "ubigeo"

    id: Mapped[str] = mapped_column(String(6), primary_key=True, nullable=False, comment="Unique ubigeo identifier")
    department_name: Mapped[str] = mapped_column(String(50), nullable=False, comment="Department name")
    province_name: Mapped[str] = mapped_column(String(50), nullable=False, comment="Province name")
    district_name: Mapped[str] = mapped_column(Text, nullable=False, comment="District name")
    department_code: Mapped[str] = mapped_column(String(2), nullable=False, comment="Department code")
    province_code: Mapped[str] = mapped_column(String(4), nullable=False, comment="Province code")


@dataclass
class DepartmentDTO:
    department_code: str
    department_name: str


@dataclass
class ProvinceDTO:
    province_code: str
    province_name: str


@dataclass
class DistrictDTO:
    id: str
    district_name: str


@dataclass
class UbigeoDTO:
    code: str
    name: str