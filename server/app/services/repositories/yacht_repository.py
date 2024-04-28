from app.models.entities.yacht import YachtEntity
from app.services.repositories.repository import Repository
from sqlalchemy.exc import IntegrityError


class YachtRepository(Repository):
    def insert_one(self, yacht: YachtEntity) -> YachtEntity:
        yacht_model = self.data_mapper.to_model(yacht)

        self.session.add(yacht_model)
        self.session.commit()

        return self.data_mapper.to_entity(model=yacht_model)
        