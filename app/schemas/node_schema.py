from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class NodeRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None)

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)


class NodeResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    active: bool

    model_config = ConfigDict(from_attributes=True, populate_by_name=True, alias_generator=to_camel)
