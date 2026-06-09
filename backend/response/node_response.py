from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

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
    created_time: str
    updated_time: str

    model_config = {
        "from_attributes": True  # Pydantic v2 equivalent of orm_mode
    }


class NodeListResponse(BaseModel):
    nodeList: Optional[list[NodeResponse]]


class NodeCorrelationsResponse(BaseModel):
    parent_node_id: int
    destination_node_id: int
    name: str
    

    model_config = {
        "from_attributes": True  # Pydantic v2 equivalent of orm_mode
    }


class NodeCorrelationsListResponse(BaseModel):
    nodeCorrelationsList: Optional[list[NodeCorrelationsResponse]]