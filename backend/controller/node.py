from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from request.node_request import NodeRequest, NodeListRequest
from fastapi import Depends
from response.node_response import NodeResponse

from service.node_service import insert, get

router = APIRouter(prefix='/api')

@router.post('/node')
async def createNode(request: NodeListRequest) -> CommonResponse:
    print(request)
    return await insert(request)

@router.get('/node/{id}')
async def getNode(id: str, db:AsyncSession = Depends(DB.get_session)) -> CommonResponse[NodeResponse]:
    return await get(id=id, db=db)


# @router.get('/node')
# async def createNode():