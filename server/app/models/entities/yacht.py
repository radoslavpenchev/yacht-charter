from typing import Optional
from app.types.enums.yacht_type import YachtType


class YachtEntity:
    id: Optional[int] = None

    name = str
    make = str
    length = int
    width = int
    cabins = int
    passengers = int
    crew = int
    type = YachtType
    
    port_id = int