from sqlalchemy.exc import IntegrityError

from app.models.entities.user import UserEntity
from app.services.repositories.repository import Repository


class UserRepository(Repository):
    class NotUnique(Exception):
        pass
    
    def insert_one(self, user: UserEntity) -> UserEntity:
        try:
            user_model = self.data_mapper.to_model(user)

            self.session.add(user_model)
            self.session.commit()
        except IntegrityError as exc:
            self.session.rollback()
            raise self.NotUnique() from exc
