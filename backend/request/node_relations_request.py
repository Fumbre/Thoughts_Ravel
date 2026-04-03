from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

class NodeRelationsRequest(BaseModel):
    parentId: int
    nodeId: int
    spaceId: int


class NodeRelationsListRequest(BaseModel):
    nodeRelationsList: Optional[list[NodeRelationsRequest]]