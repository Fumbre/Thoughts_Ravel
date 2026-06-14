from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any
from datetime import datetime 

class NodeResponse(BaseModel):
    id: int
    name: str
    parent_id: int
    ancestor: str
    type: str
    description: Optional[str] = None
    position_x: float
    position_y: float
    shape: str
    color: str

    model_config = {
        "from_attributes": True  # Pydantic v2 equivalent of orm_mode
    }


class NodeListResponse(BaseModel):
    nodeList: Optional[list[NodeResponse]]
