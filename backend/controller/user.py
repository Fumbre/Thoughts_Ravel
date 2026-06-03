from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from fastapi import Depends
from response.user_response import UserResponse
from request.user_request import UserRegisterRequest, UserLoginRequest

from service.user_service import insertUser, login
from common.filter.user import get_current_user

from fastapi import Response


router = APIRouter(prefix='/auth')

@router.post('/register')
async def createUser(request: UserRegisterRequest, response: Response) -> CommonResponse:
    return await insertUser(request, response)


@router.post('/login')
async def loginUser(request: UserLoginRequest, response: Response, db:AsyncSession = Depends(DB.get_session)) -> CommonResponse:
    return await login(request, db, response)

@router.get('/me')
async def getUser():
    user = get_current_user()
    if not user:
        return 'nothing'
    return user


# @router.get('/user/{id}')
# async def getUser(id: str, db:AsyncSession = Depends(DB.get_session)) -> CommonResponse[UserResponse]:
    # return await get(id=id, userId=, db=db)
