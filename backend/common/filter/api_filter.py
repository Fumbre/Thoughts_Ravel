from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse
from common.response.default import CommonResponse
from common.security.token import Token
from common.redis.redis import Redis
from common.filter.user import set_current_user, clear_current_user
import json

class ApiFilter(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        white_list = ["/auth/login", "/auth/register"]
        try :

            if request.url.path in white_list:
                return await call_next(request)
            
            token_cookie = request.cookies.get("access_token")
            print(token_cookie)

            if not token_cookie:
                return JSONResponse(status_code=200, 
                                    content=CommonResponse.response(code=401, message="Not authorizated").model_dump()
                                    )

            payload = Token.verify_access_token(token_cookie)

            if not payload:
                return JSONResponse(status_code=200, 
                                    content=CommonResponse.response(code=401, message="Invalid token").model_dump()
                                    )

            if not payload.get("id"):
                return JSONResponse(status_code=200, 
                                    content=CommonResponse.response(code=401, message="Token expiered").model_dump()
                                    )
            
            result_redis = await Redis.get(payload["id"])

            if not result_redis:
                return JSONResponse(status_code=200, 
                                    content=CommonResponse.response(code=401, message="Token expiered").model_dump()
                                    )
            
            await Redis.add(payload["id"], result_redis) # update token in redis

            user = json.loads(result_redis)

            set_current_user(user)

            return await call_next(request)
            
        finally: 
            clear_current_user()
            


