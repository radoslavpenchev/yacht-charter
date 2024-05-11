from app.models.db.yacht import Yacht
from app.models.entities.yacht import YachtEntity
from app.services.date_mappers.data_mapper import DataMapper
from app.types.enums.yacht_type import YachtType


class YachtMapper(DataMapper):
    def to_model(self, entity: YachtEntity) -> Yacht:
        return Yacht(
            id = entity.id,
            name = entity.name,
            make = entity.make,
            length = entity.length,
            width = entity.width,
            cabins = entity.cabins,
            passengers = entity.passengers,
            crew = entity.crew,
            type = entity.type.value,
            price = entity.price,
            port_id = entity.port_id,
        )
    
    def to_entity(self, model: Yacht) -> YachtEntity:
        return YachtEntity(
            id = model.id,
            name = model.name,
            make = model.make,
            length = model.length,
            width = model.width,
            cabins = model.cabins,
            passengers = model.passengers,
            crew = model.crew,
            type = YachtType(model.type),
            price=model.price,
            port_id = model.port_id,
        )