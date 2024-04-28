from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import relationship

from app.models.db.base_model import BaseModel
from app.types.enums.user_role import UserRole


class User(BaseModel):
    __tablename__ = "users"

    email = Column(String, nullable= False, unique=True)
    password = Column(String, nullable=False)
    role = Column(Enum(*[role.value for role in UserRole], name="role"))

    reservations = relationship("Reservation", back_populates="user")