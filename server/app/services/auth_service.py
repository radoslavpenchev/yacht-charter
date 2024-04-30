from app.models.entities.user import UserEntity
from app.services.repositories.user_repository import UserRepository
from app.types.enums.user_role import UserRole


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, email, password, role=UserRole.USER):
        try: 
            self.user_repository.insert_one(UserEntity(
                email=email,
                password=password,
                role=role,
                )
            )
            return True
        except UserRepository.NotUnique:
            return False
        
            
