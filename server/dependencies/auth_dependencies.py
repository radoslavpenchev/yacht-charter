from fastapi import Depends, HTTPException
from app.models.entities.user import UserEntity
from app.services.auth_service import AuthService
from app.services.repositories.user_repository import UserRepository
from dependencies.repositories_loaders import get_user_repository


async def get_auth_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repository=user_repository)
