from sqlalchemy.orm import Session

from app.models.zone import Zone
from app.repositories.base_repository import BaseRepository


class ZoneRepository(BaseRepository[Zone, int]):

    def __init__(self, session: Session):
        super().__init__(session, Zone)
