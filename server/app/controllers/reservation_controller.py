from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.entities.reservation import ReservationEntity
from app.models.entities.user import UserEntity
from app.services.repositories.reservation_repository import ReservationRepository
from app.types.dtos.reservation_dtos import CreateReservationPayload, CreateReservationResponse
from dependencies.auth_dependencies import get_current_user
from dependencies.repositories_loaders import get_reservation_repository


reservation_controller = APIRouter(prefix="/reservations")


@reservation_controller.post("/", response_model=CreateReservationResponse)
def create_reservation(
    body: CreateReservationPayload,
    current_user: Annotated[UserEntity, Depends(get_current_user)],
    reservation_repository: Annotated[
        ReservationRepository, Depends(get_reservation_repository)],
):
    reservation = ReservationEntity(
        start_date = body.start_date,
        end_date = body.end_date,
        user_id = current_user.id,
        yacht_id = body.yacht_id,
    )

    reservation_repository.insert_one(reservation=reservation)

    return {"message": f"successfully added a reservation for {reservation.start_date} - {reservation.end_date}"}