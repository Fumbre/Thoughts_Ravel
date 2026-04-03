from sqlalchemy import select
from request.node_relations_request import NodeRelationsRequest, NodeRelationsListRequest
from decorators.decor import Transactional
from model.node import NodesRelations
from common.db.session import AsyncSession
from common.response.default import CommonResponse

from response.node_relations_response import NodeRelationsResponse, NodeRelationsListResponse

@Transactional
async def insert(request: NodeRelationsListRequest, db: AsyncSession) -> CommonResponse:
    emptyList = []
    for node in request.nodeRelationsList :
        emptyList.append(NodesRelations(**node.model_dump()))

    db.add_all(emptyList)
    

    return CommonResponse.success()

async def get(spaceId: str, db: AsyncSession) -> CommonResponse[NodeRelationsListRequest]:
    data = await db.scalars(select(NodesRelations).where(NodesRelations.spaceId == int(spaceId)))

    results = data.all()
    results = [NodeRelationsResponse.model_validate(row) for row in results]

    for result in results:
        result.parentId = str(result.parentId)
        result.nodeId = str(result.nodeId)
        result.spaceId = str(result.spaceId)

    return CommonResponse.success(data=NodeRelationsListResponse(nodeRelationsList=results))

