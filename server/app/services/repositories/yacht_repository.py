from typing import List
from app.models.db.yacht import Yacht
from app.models.entities.yacht import YachtEntity
from app.services.repositories.repository import Repository
from sqlalchemy.exc import IntegrityError, NoResultFound

from app.types.enums.country import Country

class YachtRepository(Repository):
    class NotFound(Exception):
        def __init__(self, yacht_id: int):
            super().__init__(f"Yacht with id {yacht_id} not found")

    class AlreadyExists(Exception):
        def __init__(self, yacht_id: int):
            super().__init__(f"Yacht already exists")

    def insert_one(self, yacht: YachtEntity) -> YachtEntity:
        yacht_model = self.data_mapper.to_model(yacht)

        self.session.add(yacht_model)
        self.session.commit()

        return self.data_mapper.to_entity(model=yacht_model)
        
    def update_yacht(self, yacht: YachtEntity) -> YachtEntity:
        current_yacht = self.session.get(Yacht, yacht.id)
        if current_yacht is None:
            raise self.NotFound(yacht_id = yacht.id)
        try:
            merged_yacht = self.session.merge(
                self.data_mapper.to_model(yacht))
            self.session.commit()
            return self.data_mapper.to_entity(model=merged_yacht)
        except IntegrityError as exc:
            raise self.AlreadyExists(yacht_id = yacht.id) from exc
        
    def get_all(self) -> List[YachtEntity]:
        yachts = self.session.query(Yacht).all()

        return self.data_mapper.to_entities(yachts)
    
    def get_by_port(self, port_id: int) -> List[YachtEntity]:
        yachts = self.session.query(Yacht).filter(Yacht.port_id == port_id).all()

        return self.data_mapper.to_entities(yachts)
    def get_by_country(self, country: str) -> List[YachtEntity]:
        yachts = self.session.query(Yacht
                ).join(Yacht.port).filter(Yacht.port.country == country).all()

        return self.data_mapper.to_entities(yachts)
    
    def remove_one(self, yacht_id: int):
        try:
            yacht = self.session.get(YachtEntity, yacht_id)
            self.session.delete(yacht)
            self.session.commit()
        except NoResultFound as exc:
            raise self.NotFound(yacht_id = yacht_id) from exc