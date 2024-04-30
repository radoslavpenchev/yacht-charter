import dataclasses
from typing import Optional


@dataclasses.dataclass
class ReservationEntity:
    start_date: str
    end_date: str
    user_id: int
    yacht_id: int

    id: Optional[int]= None

    