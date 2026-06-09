from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

class SpaceRequest(BaseModel):
    name: str
    creater_id: int


class SpaceListRequest(BaseModel):
    spaceList: Optional[list[SpaceRequest]]