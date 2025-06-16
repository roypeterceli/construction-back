from typing import Optional, List

from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.config.service_config import service_provider
from app.schemas.api_response import ApiResponse
from app.schemas.feature_schema import FeatureResponse, FeatureRequest
from app.utils.jwt_util import jwt_bearer

router = APIRouter(
    prefix="/v1/features",
    tags=["Feature"]
)


@router.post("",
             summary="Create a new feature",
             status_code=HTTP_201_CREATED,
             response_model=ApiResponse[FeatureResponse],
             dependencies=[Depends(jwt_bearer)]
             )
def create_feature(request: FeatureRequest):
    with service_provider.feature_service() as feature_service:
        return ApiResponse.ok(feature_service.create(request))


@router.put("/{feature_id}",
            summary="Update a feature by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[FeatureResponse],
            dependencies=[Depends(jwt_bearer)]
            )
def update_feature(feature_id: int, request: FeatureRequest):
    with service_provider.feature_service() as feature_service:
        return ApiResponse.ok(feature_service.update(feature_id, request))


@router.get("",
            summary="Get all features",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[List[FeatureResponse]]
            )
def get_all_features():
    with service_provider.feature_service() as feature_service:
        return ApiResponse.ok(feature_service.get_all())


@router.get("/{feature_id}",
            summary="Get feature by id",
            status_code=HTTP_200_OK,
            response_model=ApiResponse[Optional[FeatureResponse]]
            )
def get_feature_by_id(feature_id: int):
    with service_provider.feature_service() as feature_service:
        return ApiResponse.ok(feature_service.get_by_id(feature_id))
