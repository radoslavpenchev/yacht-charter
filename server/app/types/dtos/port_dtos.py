from pydantic import BaseModel

from app.types.enums.country import Country
from app.types.enums.town import Town


class CreatePortPayload(BaseModel):
    name: str
    country: Country
    town: Town

class CreatePortResponse(BaseModel):
    message: str

class DeletePortResponse(BaseModel):
    message: str