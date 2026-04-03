from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from request.space_request import SpaceRequest, SpaceListRequest
from fastapi import Depends
from response.space_response import SpaceResponse, SpaceListResponse

from service.space_service import insert, get, get_all


CURRENT_USER_ID = "1"  # mock, replace with JWT later

router = APIRouter(prefix='/api')

@router.post('/space')
async def createSpace(request: SpaceListRequest) -> CommonResponse:
    return await insert(request)

@router.get('/space/{id}')
async def getSpace(id: str, db:AsyncSession = Depends(DB.get_session)) -> CommonResponse[SpaceResponse]:
    return await get(id=id, userId=CURRENT_USER_ID, db=db)

@router.get('/space')
async def getSpaces(db:AsyncSession = Depends(DB.get_session)) -> CommonResponse[SpaceListResponse]:
    return await get_all(userId=CURRENT_USER_ID, db=db)


# future to add:
# from common.auth import get_current_user  # - auth dependency
#
# example:
#
# @router.get('/spaces')
# async def getSpaces(
#    db: AsyncSession = Depends(DB.get_session),
#    current_user = Depends(get_current_user)  # extracts userId from token
# ):
#    return await get_all(userId=str(current_user.id), db=db)