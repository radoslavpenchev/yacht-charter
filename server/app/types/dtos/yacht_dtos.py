from pydantic import BaseModel

from app.types.enums.yacht_type import YachtType


class CreateYachtPayload(BaseModel):
    name: str
    make: str
    length: int
    width: int
    cabins: int
    passengers: int
    crew: int
    type: YachtType    
    port_id: int

class CreateYachtResponse(BaseModel):
    message: str

class UpdateYachtPayload(BaseModel):
    id: int
    name: str
    make: str
    length: int
    width: int
    cabins: int
    passengers: int
    crew: int
    type: YachtType
    port_id: int

class UpdateYachtResponse(BaseModel):
    message: str

class DeleteYachtResponse(BaseModel):
    message: str