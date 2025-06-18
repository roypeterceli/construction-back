from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class ZoneRequest(BaseModel):
    ubigeo_department_id: str | None = Field(default=None)
    ubigeo_province_id: str | None = Field(default=None)
    zone_code: str | None = Field(default=None)

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)


class ZoneResponse(BaseModel):
    ubigeo_department_id: str
    ubigeo_province_id: str
    zone_code: str 
    troncales: int | None = Field(default=0)
    box_naps: int | None = Field(default=0)
    advance_id: int | None = Field(default=0)
    state_id: int | None = Field(default=1)
    sale_id: int | None = Field(default=1)
    active: bool | None = Field(default=True)

    model_config = ConfigDict(from_attributes=True, populate_by_name=True, alias_generator=to_camel)
