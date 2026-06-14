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

class NodePositionUpdateRequest(BaseModel):
    id: str
    position_x: float
    position_y: float

class NodeEdgeRequest(BaseModel):
    space_id: int
    name: str
    description: Optional[str] = None
    type: str
    shape: str
    color: str
    parent_node_id: int
    parent_pos_x: float
    parent_pos_y: float
    label: Optional[str]

class NodeEdgeListRequest(BaseModel):
    nodeEdgeList: Optional[list[NodeEdgeRequest]]
    