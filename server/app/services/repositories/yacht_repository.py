import dataclasses
from typing import List, Optional
from app.models.db.port import Port
from app.models.db.yacht import Yacht
from app.models.entities.yacht import YachtEntity
from app.services.repositories.repository import Repository
from sqlalchemy.exc import IntegrityError, NoResultFound

from app.types.enums.country import Country
from app.types.enums.yacht_type import YachtType

@dataclasses.dataclass
class YachtFilters:
    port_id: Optional[int] = None
    country: Optional[Country] = None
    length: Optional[int] = None
    passengers: Optional[int] = None
    type: Optional[YachtType] = None

    def to_filter(self):
        filters = []
        if self.port_id:
            filters.append(Yacht.port_id == self.port_id)
        if self.country:
            filters.append(Port.country == self.country)
        if self.length:
            filters.append(Yacht.length >= self.length)
        if self.passengers:
            filters.append(Yacht.passengers >= self.passengers)
        if self.type:
            filters.append(Yacht.type == self.type)

        return filters
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
    
    def get_yachts(self, filters: YachtFilters) -> List[YachtEntity]:
        query = (self.session.query(Yacht).join(Port))
        yachts = query.filter(*filters.to_filter()).all()

        return self.data_mapper.to_entities(yachts)
    def remove_one(self, yacht_id: int):
        try:
            yacht = self.session.get(YachtEntity, yacht_id)
            self.session.delete(yacht)
            self.session.commit()
        except NoResultFound as exc:
            raise self.NotFound(yacht_id = yacht_id) from exc