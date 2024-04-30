from app.models.entities.reservation import ReservationEntity
from app.services.repositories.repository import Repository


class ReservationRepository(Repository):
    def insert_one(self, reservation: ReservationEntity) -> ReservationEntity:
        reservation_model = self.data_mapper.to_model(reservation)

        self.session.add(reservation_model)
        self.session.commit()

        return self.data_mapper.to_entity(model=reservation_model)