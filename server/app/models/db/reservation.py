from sqlalchemy import Column, DateTime
from sqlalchemy.orm import relationship
from app.models.db.base_model import BaseModel


class Reservation(BaseModel):
    __tablename__ = "reservations"

    start_date = Column(DateTime, nullable=False)    
    end_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="reservations")
    yacht = relationship("Yaht", back_populates="reservations")
    