from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any
from datetime import datetime 


class NodeCorrelationsResponse(BaseModel):
    parent_node_id: int
    destination_node_id: int
    name: str
    

    model_config = {
        "from_attributes": True  # Pydantic v2 equivalent of orm_mode
    }


class NodeCorrelationsListResponse(BaseModel):
    nodeCorrelationsList: Optional[list[NodeCorrelationsResponse]]