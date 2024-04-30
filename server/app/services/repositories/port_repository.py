from app.models.entities.port import PortEntity
from app.services.repositories.repository import Repository


class PortRepository(Repository):
    def insert_one(self, port: PortEntity) -> PortEntity:
        port_model = self.data_mapper.to_model(port)

        self.session.add(port_model)
        self.session.commit()

        return self.data_mapper.to_entity(model=port_model)