from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

class NodeRelationsResponse(BaseModel):
    parentId: int
    nodeId: int
    spaceId: int
    userId: int
    public_status: str
    

    model_config = {
        "from_attributes": True  # Pydantic v2 equivalent of orm_mode
    }


class NodeRelationsListResponse(BaseModel):
    nodeRelationsList: Optional[list[NodeRelationsResponse]]