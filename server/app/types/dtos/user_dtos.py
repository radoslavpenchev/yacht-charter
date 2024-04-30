from pydantic import BaseModel


class RegisterUserPayload(BaseModel):
    email: str
    password: str

class RegisterUserResponse(BaseModel):
    message: str