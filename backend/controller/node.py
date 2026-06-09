from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from fastapi import Depends, Request, Response
from request.node_request import NodeSpaceListRequest
from service.space_service import insert


router = APIRouter(prefix='/api')


@router.post('/space')
async def createNodeSpace(request: Request, body: NodeSpaceListRequest) -> CommonResponse:
    return await insert(request = body, req = request)