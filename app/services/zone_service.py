from typing import Optional, List

from app.exceptions.not_found_exception import NotFoundException
from app.models.zone import Zone
from app.repositories.zone_repository import ZoneRepository
from app.schemas.zone_schema import ZoneRequest, ZoneResponse


class ZoneService:

    def __init__(self, zone_repository: ZoneRepository):
        self.zone_repository = zone_repository


    def get_all(self) -> List[ZoneResponse]:
        zones = self.zone_repository.find_all_zones()
        return [ZoneResponse.model_validate(zone) for zone in zones]


    def get_by_id(self, zone_id: int) -> Optional[ZoneResponse]:
        zone = self.zone_repository.find_by_id(zone_id)
        if not zone:
            raise NotFoundException(f"Zone with id {zone_id} not found")
        return ZoneResponse.model_validate(zone)


    def create(self, request: ZoneRequest) -> ZoneResponse:
        zone = Zone(**request.model_dump(exclude_none=True))
        response = self.zone_repository.save(zone)
        return ZoneResponse.model_validate(response)



    def update(self, zone_id: int, request: ZoneRequest) -> ZoneResponse:
        zone = self.zone_repository.find_by_id(zone_id)

        if not zone:
            raise NotFoundException(f"Zone with id {zone_id} not found")

        zone.zone_id = zone_id

        response = self.zone_repository.update(zone)
        return ZoneResponse.model_validate(response)


