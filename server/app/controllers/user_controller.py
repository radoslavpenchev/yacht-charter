from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.models.entities.user import UserEntity
from app.services.auth_service import AuthService
from app.services.repositories.user_repository import UserRepository
from app.types.dtos.user_dtos import RegisterUserPayload, RegisterUserResponse
from dependencies.auth_dependencies import get_auth_service
from dependencies.repositories_loaders import get_user_repository


user_controller = APIRouter(prefix="/users")

@user_controller.post("/", response_model= RegisterUserResponse)
def register_user(
    body: RegisterUserPayload,
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    result = auth_service.register_user(
        email=body.email,
        password=body.password, 
    )
    if not result:
        raise HTTPException(
            status_code=400, 
            detail="User already exists"
        )

    return {"message": f"Successfully registered a user with email: {body.email}"}