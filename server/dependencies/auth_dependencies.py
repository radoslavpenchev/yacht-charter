from jose import JWTError, jwt

from fastapi import Depends, HTTPException, Header
from app.models.entities.user import UserEntity
from app.services.auth_service import AuthService
from app.services.repositories.user_repository import UserRepository
from dependencies.repositories_loaders import get_user_repository

SECRET_KEY = "aP2@!0t1*lk#Hjs8F8dl&kL2nP!0t1*LKz!Xb@Qe"
ALGORITHM = "HS256"

async def get_current_user(authorization: str = Header(...),
    user_repository: UserRepository = Depends(get_user_repository),
    ) -> UserEntity:
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except (IndexError, JWTError):
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = user_repository.get_by_email(email=email)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user


async def get_auth_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repository=user_repository)
