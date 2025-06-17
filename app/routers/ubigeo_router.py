from typing import List, Optional

from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from app.config.service_config import service_provider
from app.schemas.api_response import ApiResponse
from app.schemas.ubigeo_schema import UbigeoBaseResponse, UbigeoResponse

# from app.utils.jwt_util import jwt_bearer
# from app.utils.jwt_keyclok import oauth2_scheme

router = APIRouter(
    prefix="/api/ubigeo",
    tags=["Ubigeo"]
)


@router.get("/departments",
            summary="Get all departments",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[List[UbigeoBaseResponse]]
            )
def get_all_departments():
    with service_provider.ubigeo_service() as ubigeo_service:
        return ApiResponse.ok(ubigeo_service.get_all_departments())


@router.get("/departments/{department_code}/provinces",
            summary="Get all provinces by department code",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[List[UbigeoBaseResponse]]
            )
def get_provinces_by_department(department_code: str):
    with service_provider.ubigeo_service() as ubigeo_service:
        return ApiResponse.ok(ubigeo_service.get_provinces_by_department_code(department_code))


@router.get("/departments/{department_code}/provinces/{province_code}/districts",
            summary="Get all districts by department and province code",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[List[UbigeoBaseResponse]]
            )
def get_provinces_by_department_and_province(department_code: str, province_code: str):
    with service_provider.ubigeo_service() as ubigeo_service:
        return ApiResponse.ok(ubigeo_service.get_provinces_by_department_and_province_code(department_code, province_code))


@router.get("/{id}",
            summary="Get ubigeo by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[Optional[UbigeoResponse]]
            # dependencies=[Depends(jwt_bearer)]
            )
def get_by_id(id: str):
    with service_provider.ubigeo_service() as ubigeo_service:
        return ApiResponse.ok(ubigeo_service.get_by_id(id))
    
