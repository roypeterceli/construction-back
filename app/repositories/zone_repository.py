from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.zone import Zone, ZoneDTO
from app.repositories.base_repository import BaseRepository

class ZoneRepository(BaseRepository[Zone, int]):

    def __init__(self, session: Session):
        super().__init__(session, Zone)


    def find_all_zones(self) -> List[ZoneDTO]:
        query = (
            select(Zone.zone_id, Zone.troncales)
            .distinct(Zone.zone_id)
            .order_by(Zone.zone_id.asc())
        )
        result = self.session.execute(query).all()
        return [ZoneDTO(code=code, troncales=troncales) for code, troncales in result]
    
    
    def find_by_id(self, id: int) -> Zone | None:
        return self.session.get(Zone, id)
    

    def save(self, zone: Zone) -> Zone:
        self.session.add(zone)
        self.session.commit()
        self.session.refresh(zone)
        return zone