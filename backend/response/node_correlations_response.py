from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class NodeCorrelationResponse(BaseModel):
    # Enables automatic mapping from SQLAlchemy ORM objects
    model_config = ConfigDict(from_attributes=True)

    parent_node_id: int
    destination_node_id: int
    name: str
    description: Optional[str] = None
    type: Optional[str] = '0'

class NodeCorrelationsListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    # Defaults to an empty list if no correlations are present
    nodeCorrelationsList: List[NodeCorrelationResponse] = []