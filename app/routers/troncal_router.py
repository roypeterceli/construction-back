from typing import Optional, List

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.config.service_config import service_provider
from app.schemas.api_response import ApiResponse
from app.schemas.troncal_schema import TroncalResponse, TroncalRequest
from app.utils.jwt_util import jwt_bearer

router = APIRouter(
    prefix="/api/troncals",
    tags=["Troncal"]
)


@router.post("",
             summary="Create a new troncal",
             status_code=HTTP_201_CREATED,
             response_model=ApiResponse[TroncalResponse],
             dependencies=[Depends(jwt_bearer)]
             )
def create_troncal(request: TroncalRequest):
    with service_provider.troncal_service() as troncal_service:
        return ApiResponse.ok(troncal_service.create(request))


@router.put("/{troncal_id}",
            summary="Update a troncal by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[TroncalResponse],
            dependencies=[Depends(jwt_bearer)]
            )
def update_troncal(troncal_id: int, request: TroncalRequest):
    with service_provider.troncal_service() as troncal_service:
        return ApiResponse.ok(troncal_service.update(troncal_id, request))


@router.get("",
            summary="Get all troncals",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[List[TroncalResponse]]
            )
def get_all_troncals():
    with service_provider.troncal_service() as troncal_service:
        return ApiResponse.ok(troncal_service.get_all())


@router.get("/{troncal_id}",
            summary="Get troncal by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[Optional[TroncalResponse]]
            )
def get_troncal_by_id(troncal_id: int):
    with service_provider.troncal_service() as troncal_service:
        return ApiResponse.ok(troncal_service.get_by_id(troncal_id))
