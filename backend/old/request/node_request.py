from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any


class NodeSpaceRequest(BaseModel):
    name: str
    parent_id: int

class NodeSpaceListRequest(BaseModel):
    nodeList: Optional[list[NodeSpaceRequest]]


class NodeRequest(BaseModel):
    name: str
    desc: Optional[str] = None
    positionX: float
    positionY: float
    color: str
    shape: str
    creater_id: int

class NodeParentRequest(BaseModel):
    nodeId: int
    spaceId: int
    userId: int
    public_status: str

class NodeListRequest(BaseModel):
    nodeList: Optional[list[NodeRequest]]


class NodeConnectionRequest(BaseModel):
    name: str
    desc: Optional[str]
    positionX: float
    positionY: float
    color: str
    shape: str
    creater_id: str
    nodeId: str
    spaceId: str
    userId: str
