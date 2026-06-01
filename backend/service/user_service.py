from sqlalchemy import select, or_
from request.user_request import  UserRegisterRequest, UserLoginRequest
from decorators.decor import Transactional
from model.user import User
from common.db.session import AsyncSession
from common.response.default import CommonResponse
from common.id.snowflake_id_util import getId

from common.security.pwd import hash_password, verify_password


from response.user_response import UserResponse

@Transactional
async def insertUser(request: UserRegisterRequest, db: AsyncSession) -> CommonResponse:
    email = await getUserInfo(request.email, db)
    if email:
        return CommonResponse.faild(message="email is exist")
    username = await getUserInfo(request.username, db)

    if username:
        return CommonResponse.faild(message="username is exist")
    
    pwd_hashed =  hash_password(request.password)

    user = User(
        username = request.username,
        email = request.email,
        password = pwd_hashed
    )

    print(user)

    db.add(user)

    return CommonResponse.success()



# do redis later
async def getUserInfo(login: str, db: AsyncSession) -> User:
    data = await db.scalar(select(User).where( or_ (User.email == login, User.username == login) ))

    return data


async def login(request: UserLoginRequest, db: AsyncSession) -> CommonResponse:
    user = await getUserInfo(request.login, db)
    if not user:
        return CommonResponse.faild(message="User doesn't exist")

    is_pwd_match =  verify_password(request.password, user.password)

    if not is_pwd_match:
        return CommonResponse.faild(message="User or password is not correct")
        


    return CommonResponse.success()