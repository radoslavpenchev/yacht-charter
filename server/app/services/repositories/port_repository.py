from typing import List
from app.models.db.port import Port
from app.models.entities.port import PortEntity
from app.services.repositories.repository import Repository
from sqlalchemy.exc import IntegrityError, NoResultFound



class PortRepository(Repository):
    class NotFound(Exception):
        def __init__(self, port_id: int):
            super().__init__(f"Port with id {port_id} not found")

    class AlreadyExists(Exception):
        def __init__(self, port_id: int):
            super().__init__(f"Port with id {port_id} already exists")

    def insert_one(self, port: PortEntity) -> PortEntity:
        try:
            port_model = self.data_mapper.to_model(port)
            self.session.add(port_model)
            self.session.commit()
            return self.data_mapper.to_entity(model=port_model)
        except IntegrityError as exc:
            raise self.AlreadyExists(port_id = port.id) from exc
    
    def remove_one(self, port_id: int):
        try:
            port = self.session.get(Port, port_id)
            self.session.delete(port)
            self.session.commit()
        except NoResultFound as exc:
            raise self.NotFound(port_id = port_id) from exc
