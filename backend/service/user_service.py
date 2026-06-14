from sqlalchemy import select, or_
from request.user_request import  UserRegisterRequest, UserLoginRequest
from response.user_response import UserResponse
from decorators.decor import Transactional
from model.user import User
from common.db.session import AsyncSession
from common.response.default import CommonResponse
from common.id.snowflake_id_util import getId
from common.filter.user import get_current_user
from common.security.pwd import hash_password, verify_password

from common.security.token import Token
from common.redis.redis import Redis

from fastapi import Response, Request


import datetime
import json

async def login(request: UserLoginRequest, db: AsyncSession, response: Response) -> CommonResponse:
    user = await getUserInfo(request.login, db)
    if not user:
        return CommonResponse.faild(message="User doesn't exist")

    is_pwd_match = verify_password(request.password, user.password)

    if not is_pwd_match:
        return CommonResponse.faild(message="User or password is not correct")
        
    cool_user = UserResponse.model_validate(user).model_dump()


    token = await createToken(cool_user, response)


    return CommonResponse.success(data=cool_user)


@Transactional
async def insertUser(request: UserRegisterRequest, response: Response, db: AsyncSession,) -> CommonResponse:
    email = await getUserInfo(request.email, db)
    if email:
        return CommonResponse.faild(message="email is exist")
    username = await getUserInfo(request.username, db)

    if username:
        return CommonResponse.faild(message="username is exist")
    
    pwd_hashed =  hash_password(request.password)

    user = User(
        id=getId(),
        username=request.username,
        email=request.email,
        password=pwd_hashed,
        status="0"
    )

    db.add(user)
    cool_user_model = UserResponse.model_validate(user) 
    user_dict = cool_user_model.model_dump() # Converts model parameters into a clean dict

    token = await createToken(user_dict, response)
    
    return CommonResponse.success(data=user_dict)


async def getUserInfo(login: str, db: AsyncSession) -> User:
    data = await db.scalar(select(User).where( or_ (User.email == login, User.username == login) ))

    return data

async def logout(request: Request, response: Response) -> CommonResponse:
    user = get_current_user(request)
    if not user:
        return CommonResponse.faild(message="Not authenticated")
    
    await Redis.remove(user["id"])  # remove session from Redis
    
    response.delete_cookie(
        key="access_token",
        httponly=True,
        secure=False,  # match your createCookie settings
        samesite="lax",
        path="/"
    )
    
    return CommonResponse.success(message="Logged out")


async def createToken(payload: dict, response: Response) -> str:
    expired_time = 60*60

    time_stamp = datetime.datetime.now().timestamp()
    payload["time_stamp"] = time_stamp
    token = Token.create_access_token(payload)

    if "password" in payload.keys() :
        del payload["password"] # delete password for security

    await Redis.add(str(payload["id"]), json.dumps(payload), expired_time)

    createCookie(response, token, expired_time)
    
    return token
 

def createCookie(response: Response, token, expired_time):

    return response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,       
        secure=False,         # False for localhost dev | but for prod
        samesite="lax",     
        max_age=expired_time,       
        path="/"             
    )