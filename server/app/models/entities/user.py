import dataclasses
from typing import Optional

from app.types.enums.user_role import UserRole


@dataclasses.dataclass
class UserEntity:
    password: str
    email: str
    role: UserRole

    id: Optional[int]= None