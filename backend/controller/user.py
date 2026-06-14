from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from fastapi import Depends, Request
from response.user_response import UserResponse
from request.user_request import UserRegisterRequest, UserLoginRequest

from service.user_service import insertUser, login, logout
from common.filter.user import get_current_user

from fastapi import Response


router = APIRouter(prefix='/auth')

@router.post('/register')
async def createUser(request: UserRegisterRequest, response: Response) -> CommonResponse:
    return await insertUser(request, response)

@router.post('/logout')
async def logoutUser(request: Request, response: Response) -> CommonResponse:
    return await logout(request, response)

@router.post('/login')
async def loginUser(request: UserLoginRequest, response: Response, db:AsyncSession = Depends(DB.get_session)) -> CommonResponse:
    return await login(request, db, response)

@router.get('/me')
async def getUser(request: Request):
    user = get_current_user(request)
    if not user:
        return CommonResponse.faild(message="Not authenticated")
    return CommonResponse.success(data=user)

