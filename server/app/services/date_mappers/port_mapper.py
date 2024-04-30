from app.models.db.port import Port
from app.models.entities.port import PortEntity
from app.types.enums.country import Country
from app.types.enums.town import Town


class PortMapper:
    def to_model(self, entity: PortEntity) -> Port:
        return Port(
            id=entity.id,
            name=entity.name,
            country=entity.country.value,
            town=entity.town.value,
        )
    
    def to_entity(self, model: Port) -> PortEntity:
        return PortEntity(
            id=model.id,
            name=model.name,
            country=Country(model.country),
            town=Town(model.town),
        )