from typing import List, Optional

from app.exceptions.not_found_exception import NotFoundException
from app.repositories.ubigeo_repository import UbigeoRepository
from app.schemas.ubigeo_schema import UbigeoBaseResponse, UbigeoResponse


class UbigeoService:
    def __init__(self, repository: UbigeoRepository):
        self.ubigeo_repository = repository

    def get_by_id(self, ubigeo_id) -> Optional[UbigeoResponse]:
        ubigeo = self.ubigeo_repository.find_by_id(ubigeo_id)

        if not ubigeo:
            raise NotFoundException(f"Ubigeo with id {ubigeo_id} not found")

        return UbigeoResponse.model_validate(ubigeo)

    def get_all_departments(self) -> List[UbigeoBaseResponse]:
        departments = self.ubigeo_repository.find_all_departments()
        return [
            UbigeoBaseResponse(
                code=item.department_code,
                name=item.department_name
            )
            for item in departments
        ]

    def get_provinces_by_department_code(self, department_code: str) -> List[UbigeoBaseResponse]:
        provinces = self.ubigeo_repository.find_provinces_by_department_code(department_code)
        return [
            UbigeoBaseResponse(
                code=item.province_code,
                name=item.province_name
            )
            for item in provinces
        ]

    def get_provinces_by_department_and_province_code(
            self, department_code: str, province_code: str
    ) -> List[UbigeoBaseResponse]:
        districts = self.ubigeo_repository.find_districts_by_department_and_province_code(
            department_code,
            province_code
        )
        return [
            UbigeoBaseResponse(
                code=item.id,
                name=item.district_name
            )
            for item in districts
        ]