from sqlalchemy.exc import IntegrityError, NoResultFound

from app.models.db.user import User
from app.models.entities.user import UserEntity
from app.services.repositories.repository import Repository


class UserRepository(Repository):
    class NotFound(Exception):
        def __init__(self, user_id: int):
            super().__init__(f"User with id {user_id} not found")
    
    class AlreadyExists(Exception):
        def __init__(self, user_id: int):
            super().__init__(f"User with id {user_id} already exists")

    
    def insert_one(self, user: UserEntity) -> UserEntity:
        try:
            user_model = self.data_mapper.to_model(user)

            self.session.add(user_model)
            self.session.commit()
            return self.data_mapper.to_entity(model=user_model)
        except IntegrityError as exc:
            raise self.AlreadyExists(user_id = user.id) from exc
        
    def get_by_email(self, email: str) -> UserEntity:
        try:
            user = self.session.query(User).filter_by(User.email == email).one()
            return self.data_mapper.to_entity(user)
        except NoResultFound as exc:
            return None
        
    def update_user(self, user: UserEntity):
        if user.id is None:
            raise self.NotFound(user_id=user.id)

        existing_user = self.session.get(User, user.id)

        if existing_user is None:
            raise self.NotFound(user_id=user.id)

        self.session.merge(self.data_mapper.to_model(entity=user))
        self.session.commit()

        return user