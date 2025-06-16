from requests import Session

from app.models.feature import Feature
from app.repositories.base_repository import BaseRepository


class FeatureRepository(BaseRepository[Feature, int]):

    def __init__(self, session: Session):
        super().__init__(session, Feature)
