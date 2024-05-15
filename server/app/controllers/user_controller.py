from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.services.auth_service import AuthService
from app.types.dtos.user_dtos import RegisterUserPayload, RegisterUserResponse
from dependencies.auth_dependencies import get_auth_service


user_controller = APIRouter(prefix="/users")

@user_controller.post("/", response_model= RegisterUserResponse)
def register_user(
    body: RegisterUserPayload,
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