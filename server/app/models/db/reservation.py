from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.models.db.base_model import BaseModel


class Reservation(BaseModel):
    __tablename__ = "reservations"

    start_date = Column(DateTime, nullable=False)    
    end_date = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    yacht_id = Column(Integer, ForeignKey("yachts.id"), nullable=False)

    user = relationship("User", back_populates="reservations")
    yacht = relationship("Yacht", back_populates="reservations")
    