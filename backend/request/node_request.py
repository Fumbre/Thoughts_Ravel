from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any


class NodeSpaceRequest(BaseModel):
    name: str
    parent_id: int
    ancestor:  Optional[str] = '0'
    description: Optional[str] = None
    type: str
    position_x: float
    position_y: float
    shape: str
    color: str

class NodeSpaceListRequest(BaseModel):
    nodeSpaceList: Optional[list[NodeSpaceRequest]]