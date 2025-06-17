from typing import Optional, List

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.config.service_config import service_provider
from app.schemas.api_response import ApiResponse
from app.schemas.naps_schema import NapsResponse, NapsRequest
from app.utils.jwt_util import jwt_bearer

router = APIRouter(
    prefix="/naps",
    tags=["Naps"]
)


@router.get("",
            summary="Get all naps",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[List[NapsResponse]]
            )
def get_all_naps():
    with service_provider.naps_service() as naps_service:
        return ApiResponse.ok(naps_service.get_all())


@router.get("/{naps_id}",
            summary="Get naps by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[Optional[NapsResponse]]
            )
def get_naps_by_id(naps_id: int):
    with service_provider.naps_service() as naps_service:
        return ApiResponse.ok(naps_service.get_by_id(naps_id))
