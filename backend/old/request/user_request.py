from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

class UserRegisterRequest(BaseModel):
    email: str
    username: str
    password: str

class UserLoginRequest(BaseModel):
    login: str
    password: str


