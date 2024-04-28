from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import relationship
from app.models.db.base_model import BaseModel
from app.types.enums.country import Country
from app.types.enums.town import Town


class Port(BaseModel):
    __tablename__ = "ports"

    name = Column(String, nullable=False, unique=True)
    country = Column(Enum(*[country.value for country in Country], name="country"))
    town = Column(Enum(*[town.value for town in Town], name="town"))

    yachts = relationship("Yacht", back_populates="port")

    