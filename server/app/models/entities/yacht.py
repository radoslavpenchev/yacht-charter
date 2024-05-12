import dataclasses
from typing import Optional
from app.types.enums.yacht_type import YachtType

@dataclasses.dataclass
class YachtEntity:
    name: str
    make: str
    length: int
    width: int
    cabins: int
    passengers: int
    crew: int
    type: YachtType
    price: int
    port_id: int

    id: Optional[int]= None
