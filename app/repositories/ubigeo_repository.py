from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.ubigeo import Ubigeo, UbigeoDTO
from app.repositories.base_repository import BaseRepository


class UbigeoRepository(BaseRepository[Ubigeo, str]):

    def __init__(self, session: Session):
        super().__init__(session, Ubigeo)

    def find_all_departments(self) -> List[UbigeoDTO]:
        query = (
            select(Ubigeo.department_code, Ubigeo.department_name)
            .distinct(Ubigeo.department_code)
            .order_by(Ubigeo.department_code.asc())
        )
        result = self.session.execute(query).all()
        return [UbigeoDTO(code=code, name=name) for code, name in result]

    def find_provinces_by_department_code(self, department_code: str) -> List[UbigeoDTO]:
        query = (
            select(Ubigeo.province_code, Ubigeo.province_name)
            .distinct(Ubigeo.province_code)
            .where(Ubigeo.department_code == department_code)
            .order_by(Ubigeo.province_code.asc())
        )
        result = self.session.execute(query).all()
        return [UbigeoDTO(code=code, name=name) for code, name in result]

    def find_districts_by_department_and_province_code(
            self, department_code: str, province_code: str
    ) -> List[UbigeoDTO]:
        query = (
            select(Ubigeo.id, Ubigeo.district_name)
            .where(Ubigeo.department_code == department_code)
            .where(Ubigeo.province_code == province_code)
            .order_by(Ubigeo.id.asc())
        )
        result = self.session.execute(query).all()
        return [UbigeoDTO(code=code, name=name) for code, name in result]
 