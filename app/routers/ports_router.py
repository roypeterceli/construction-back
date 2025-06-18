from typing import Optional, List

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.config.service_config import service_provider
from app.schemas.api_response import ApiResponse
from app.schemas.ports_schema import PortsResponse, PortsRequest
from app.utils.jwt_util import jwt_bearer

router = APIRouter(
    prefix="/api/ports",
    tags=["Ports"]
)

@router.get("",
            summary="Get all ports",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[List[PortsResponse]]
            )
def get_all_ports():
    with service_provider.ports_service() as port_service:
        return ApiResponse.ok(port_service.get_all())


@router.get("/{port_id}",
            summary="Get port by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[Optional[PortsResponse]]
            )
def get_port_by_id(port_id: int):
    with service_provider.ports_service() as port_service:
        return ApiResponse.ok(port_service.get_by_id(port_id))
