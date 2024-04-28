from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.db.base_model import BaseModel
from app.types.enums.yacht_type import YachtType


class Yacht(BaseModel):
    __tablename__ = "yachts"

    name = Column(String, nullable=False, unique=True)
    make = Column(String, nullable=False, unique=True)
    length = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    cabins = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    type = Column(Enum(*[type.value for type in YachtType], name="yacht_type"))
    
    port_id = Column(Integer, ForeignKey("ports.id"), nullable=False)

    port = relationship("Port", back_populates="yachts")
    reservations = relationship("Reservation", back_populates="yacht")