from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

class SpaceRequest(BaseModel):
    userId: int
    title: str


class SpaceListRequest(BaseModel):
    spaceList: Optional[list[SpaceRequest]]