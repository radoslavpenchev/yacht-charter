import dataclasses
from typing import Optional

from app.types.enums.country import Country
from app.types.enums.town import Town


@dataclasses.dataclass
class PortEntity:
    name: str
    country: Country
    town: Town

    id: Optional[int] = None