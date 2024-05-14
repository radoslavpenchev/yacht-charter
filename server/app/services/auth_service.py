import bcrypt
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
                password=self.get_password_hash(password),
                role=role,
                )
            )
            return True
        except UserRepository.AlreadyExists:
            return False
        
    def update_user_password(self, user: UserEntity, new_password: str):
        new_password_hashed = self.get_password_hash(new_password)
        user.password = new_password_hashed
        return self.user_repository.update_user(user=user)

    def hash_passsword(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password = bytes(password, 'utf-8'), salt = salt)

    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(password = bytes(password, 'utf-8'), hashedpassword = hashed_password)
    
    def get_password_hash(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password=bytes(password, "utf-8"), salt=salt)

    def authenticate_user(self, username: str, password: str):
        user = self.user_repository.get_by_email(email=username)
        if user is None:
            return False

        if not self.verify_password(password, user.password):
            return False

        return user