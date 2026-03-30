from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

class NodeRequest(BaseModel):
    name: str
    desc: Optional[str] = None
    positionX: float
    positionY: float
    color: str
    shape: str


class NodeListRequest(BaseModel):
    nodeList: Optional[list[NodeRequest]]