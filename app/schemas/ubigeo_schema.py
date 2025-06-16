from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class UbigeoBaseResponse(BaseModel):
    code: str | None
    name: str | None

    model_config = ConfigDict(from_attributes=True, populate_by_name=True, alias_generator=to_camel)

class UbigeoResponse(BaseModel):
    ubigeo_id: str
    department_name: str
    province_name: str
    district_name: str

    model_config = ConfigDict(from_attributes=True, populate_by_name=True, alias_generator=to_camel)