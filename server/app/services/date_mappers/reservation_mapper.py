from datetime import datetime
from app.models.db.reservation import Reservation
from app.models.entities.reservation import ReservationEntity
from app.services.date_mappers.data_mapper import DataMapper


class ReservationMapper(DataMapper):
    def to_model(self, entity: ReservationEntity) -> Reservation:
        return Reservation(
            start_date=datetime.strptime(entity.start_date, "%Y-%m-%d"),
            end_date=datetime.strptime(entity.end_date, "%Y-%m-%d"),
            user_id=entity.user_id,
            yacht_id=entity.yacht_id
        )

    def to_entity(self, model: Reservation) -> ReservationEntity:
        return ReservationEntity(
            start_date=model.start_date,
            end_date=model.end_date,
            user_id=model.user_id,
            yacht_id=model.yacht_id
        )