from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

class SpaceResponse(BaseModel):
    id: int
    userId: int
    title: str

    model_config = {
        "from_attributes": True  # Pydantic v2 equivalent of orm_mode
    }


class SpaceListResponse(BaseModel):
    spaceList: Optional[list[SpaceResponse]]