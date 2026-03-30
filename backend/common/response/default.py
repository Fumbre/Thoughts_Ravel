from __future__ import annotations
from typing import TypeVar, Optional, Generic, Type, Callable, Any
from pydantic import BaseModel

T = TypeVar("T")

class CommonResponse(BaseModel, Generic[T]):
    code: int = None
    data: Optional[T]  = None
    message: str = None

    @classmethod
    def success(cls, code: int = 200, data: Optional[T] = None, message: str = 'Success') -> CommonResponse[T]:
        return cls(code=code, data=data, message=message)

    @classmethod
    def response(cls, code: int = None, data: Optional[T] = None, message = None) -> CommonResponse[T]:
        return cls(code=code, data=data, message=message)

    @classmethod
    def faild(cls, code: int = 500, data: Optional[T] = None, message = 'Faild') -> CommonResponse[T]:
        return cls(code=code, data=data, message=message)

