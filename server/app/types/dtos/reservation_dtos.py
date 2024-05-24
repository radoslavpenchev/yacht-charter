from pydantic import BaseModel


class CreateReservationPayload(BaseModel):
    start_date: str
    end_date: str
    yacht_id: int
    
class CreateReservationResponse(BaseModel):
    message: str