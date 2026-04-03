from sqlalchemy import select
from request.node_request import NodeRequest, NodeListRequest
from decorators.decor import Transactional
from model.node import Node
from common.db.session import AsyncSession
from common.response.default import CommonResponse

from response.node_response import NodeResponse, NodeListResponse

@Transactional
async def insert(request: NodeListRequest, db: AsyncSession) -> CommonResponse:
    emptyList = []
    for node in request.nodeList :
        emptyList.append(Node(**node.model_dump()))

    db.add_all(emptyList)
    

    return CommonResponse.success()

async def get(id: str, db: AsyncSession) -> CommonResponse[NodeResponse]:
    data = await db.scalar(select(Node).where(Node.id == int(id)))

    result = NodeResponse.model_validate(data)
    result.id = str(result.id)

    return CommonResponse.success(data=result)

