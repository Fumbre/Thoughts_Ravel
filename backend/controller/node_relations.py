from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from request.node_relations_request import NodeRelationsRequest, NodeRelationsListRequest
from fastapi import Depends
from response.node_relations_response import NodeRelationsListResponse

from service.node_relations_service import insert, get

router = APIRouter(prefix='/api')

@router.post('/node_relations')
async def createNodeRelations(request: NodeRelationsRequest) -> CommonResponse:
    return await insert(request)

@router.get('/node_relations/{spaceId}')
async def getNodeRelations(spaceId: str, db:AsyncSession = Depends(DB.get_session)) -> CommonResponse[NodeRelationsListResponse]:
    return await get(spaceId=spaceId, db=db)
