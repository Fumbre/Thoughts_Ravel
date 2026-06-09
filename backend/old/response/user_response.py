from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    status: str

    model_config = {
        "from_attributes": True  # Pydantic v2 equivalent of orm_mode
    }
