from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from fastapi import Depends
from response.user_response import UserResponse
from request.user_request import UserRegisterRequest

from service.user_service import insertUser


router = APIRouter(prefix='/auth')

@router.post('/register')
async def createUser(request: UserRegisterRequest) -> CommonResponse:
    return await insertUser(request)

# @router.get('/user/{id}')
# async def getUser(id: str, db:AsyncSession = Depends(DB.get_session)) -> CommonResponse[UserResponse]:
    # return await get(id=id, userId=, db=db)
