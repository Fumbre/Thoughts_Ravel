from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from fastapi import Depends
from response.user_response import UserResponse
from request.user_request import UserRegisterRequest, UserLoginRequest

from service.user_service import insertUser, login


router = APIRouter(prefix='/auth')

@router.post('/register')
async def createUser(request: UserRegisterRequest) -> CommonResponse:
    return await insertUser(request)


@router.post('/login')
async def loginUser(request: UserLoginRequest, db:AsyncSession = Depends(DB.get_session)) -> CommonResponse:
    return await login(request, db)

# @router.get('/user/{id}')
# async def getUser(id: str, db:AsyncSession = Depends(DB.get_session)) -> CommonResponse[UserResponse]:
    # return await get(id=id, userId=, db=db)
