from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class ZoneRequest(BaseModel):
    ubigeo_department_id: str
    ubigeo_province_id: str
    zone_code: str
    

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

class ZoneResponse(BaseModel):
    ubigeo_department_id: str
    ubigeo_province_id: str
    zone_code: str 
    troncales: int = 0
    box_naps: int = 0
    advance_id: int = 0
    state_id: int = 1
    sale_id: int = 1

    model_config = ConfigDict(from_attributes=True, populate_by_name=True, alias_generator=to_camel)
