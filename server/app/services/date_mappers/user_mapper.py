from app.models.db.user import User
from app.models.entities.user import UserEntity
from app.services.date_mappers.data_mapper import DataMapper
from app.types.enums.user_role import UserRole


class UserMapper(DataMapper):
    def to_model(self, entity: UserEntity) -> User:
        return User(
            email=entity.email,
            password=entity.password,
            role=entity.role.value,
        )

    def to_entity(self, model: User) -> UserEntity:
        return UserEntity(
            email=model.email,
            password=model.password,
            role=UserRole(model.role),
        )