from typing import Optional, List

from app.exceptions.not_found_exception import NotFoundException
from app.models.feature import Feature
from app.repositories.feature_repository import FeatureRepository
from app.schemas.feature_schema import FeatureRequest, FeatureResponse


class FeatureService:

    def __init__(self, feature_repository: FeatureRepository):
        self.feature_repository = feature_repository

    def create(self, request: FeatureRequest) -> FeatureResponse:
        feature = Feature(**request.model_dump(exclude_none=True))
        response = self.feature_repository.save(feature)
        return FeatureResponse.model_validate(response)

    def update(self, feature_id: int, request: FeatureRequest) -> FeatureResponse:
        feature = self.feature_repository.find_by_id(feature_id)

        if not feature:
            raise NotFoundException(f"Feature with id {feature_id} not found")

        feature.name = request.name
        feature.description = request.description

        response = self.feature_repository.update(feature)
        return FeatureResponse.model_validate(response)

    def get_by_id(self, feature_id: int) -> Optional[FeatureResponse]:
        feature = self.feature_repository.find_by_id(feature_id)

        if not feature:
            raise NotFoundException(f"Feature with id {feature_id} not found")

        return FeatureResponse.model_validate(feature)

    def get_all(self) -> List[FeatureResponse]:
        features = self.feature_repository.find_all()

        return [FeatureResponse.model_validate(feature) for feature in features]

