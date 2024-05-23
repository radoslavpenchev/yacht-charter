import re
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.services.auth_service import AuthService
from app.types.dtos.auth_dtos import LoginResponse
from dependencies.auth_dependencies import get_auth_service


auth_controller = APIRouter()

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validate_username(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> OAuth2PasswordRequestForm:
    if not re.match(EMAIL_REGEX, form_data.username):
        raise HTTPException(status_code=422, detail="Invalid email format")
    return form_data


@auth_controller.post("/login", response_model=LoginResponse)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends(validate_username)],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.create_access_token(
        data={"sub": user.email, "role": user.role.value}
    )
    return {"access_token": access_token, "token_type": "Bearer"}