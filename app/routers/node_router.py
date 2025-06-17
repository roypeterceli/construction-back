from typing import Optional, List

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.config.service_config import service_provider
from app.schemas.api_response import ApiResponse
from app.schemas.node_schema import NodeResponse, NodeRequest
from app.utils.jwt_util import jwt_bearer

router = APIRouter(
    prefix="/nodes",
    tags=["Node"]
)


@router.post("",
             summary="Create a new node",
             status_code=HTTP_201_CREATED,
             response_model=ApiResponse[NodeResponse],
             dependencies=[Depends(jwt_bearer)]
             )
def create_node(request: NodeRequest):
    with service_provider.node_service() as node_service:
        return ApiResponse.ok(node_service.create(request))


@router.put("/{node_id}",
            summary="Update a node by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[NodeResponse],
            dependencies=[Depends(jwt_bearer)]
            )
def update_node(node_id: int, request: NodeRequest):
    with service_provider.node_service() as node_service:
        return ApiResponse.ok(node_service.update(node_id, request))


@router.get("",
            summary="Get all nodes",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[List[NodeResponse]]
            )
def get_all_nodes():
    with service_provider.node_service() as node_service:
        return ApiResponse.ok(node_service.get_all())


@router.get("/{node_id}",
            summary="Get node by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[Optional[NodeResponse]]
            )
def get_node_by_id(node_id: int):
    with service_provider.node_service() as node_service:
        return ApiResponse.ok(node_service.get_by_id(node_id))
