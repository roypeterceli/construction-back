from typing import Optional, List

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.config.service_config import service_provider
from app.schemas.api_response import ApiResponse
from app.schemas.zone_schema import ZoneResponse, ZoneRequest
from app.utils.jwt_util import jwt_bearer

router = APIRouter(
    prefix="/zones",
    tags=["Zone"]
)


@router.post("",
             summary="Create a new zone",
             status_code=HTTP_201_CREATED,
             response_model=ApiResponse[ZoneResponse],
             dependencies=[Depends(jwt_bearer)]
             )
def create_zone(request: ZoneRequest):
    with service_provider.zone_service() as zone_service:
        return ApiResponse.ok(zone_service.create(request))


@router.put("/{zone_id}",
            summary="Update a zone by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[ZoneResponse],
            dependencies=[Depends(jwt_bearer)]
            )
def update_zone(zone_id: int, request: ZoneRequest):
    with service_provider.zone_service() as zone_service:
        return ApiResponse.ok(zone_service.update(zone_id, request))


@router.get("",
            summary="Get all zones",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[List[ZoneResponse]]
            )
def get_all_zones():
    with service_provider.zone_service() as zone_service:
        return ApiResponse.ok(zone_service.get_all())


@router.get("/{zone_id}",
            summary="Get zone by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[Optional[ZoneResponse]]
            )
def get_zone_by_id(zone_id: int):
    with service_provider.zone_service() as zone_service:
        return ApiResponse.ok(zone_service.get_by_id(zone_id))
