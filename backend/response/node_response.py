from pydantic import BaseModel
from typing import TypeVar, Optional, Generic, Type, Callable, Any

class NodeResponse(BaseModel):
    id: int
    name: str
    desc: Optional[str] = None
    positionX: float
    positionY: float
    color: str
    shape: str

    model_config = {
        "from_attributes": True  # Pydantic v2 equivalent of orm_mode
    }