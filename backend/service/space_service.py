from sqlalchemy import select
# from request.space_request import SpaceRequest, SpaceListRequest
from decorators.decor import Transactional
from model.node import Nodes
from common.db.session import AsyncSession
from common.response.default import CommonResponse
from common.id.snowflake_id_util import getId

# from service.node_service import insert as node_insert
from request.node_request import NodeSpaceListRequest, NodeSpaceRequest
from common.filter.user import get_current_user
from fastapi import Request



@Transactional
async def insert(request: NodeSpaceListRequest, db: AsyncSession, req: Request) -> CommonResponse:
    nodeSpace: NodeSpaceRequest = request.nodeSpaceList[0]

    user = get_current_user(req)
    print(user)

    ancestor = '0'

    nodeSpaceList =  []

    if nodeSpace.parent_id != 0:
        node = db.scalar(select(Nodes).where(Nodes.id == nodeSpace.parent_id))    
        ancestor = node.ancestor + ',' + nodeSpace.parent_id

    for nodeSpaceItem in request.nodeSpaceList:
        id = getId()
        nodeSpaceItem = Nodes(**nodeSpaceItem.model_dump())
        nodeSpaceItem.id = id
        nodeSpaceItem.creater_id = user["id"]
        nodeSpaceItem.ancestor = ancestor

        nodeSpaceList.append(nodeSpaceItem)

    db.add_all(nodeSpaceList)

    return CommonResponse.success()
       



async def get(id: str, userId: str, db: AsyncSession) -> CommonResponse[SpaceResponse]:
    data = await db.scalar(select(Space).where(Space.id == int(id), Space.userId == int(userId)))

    result = SpaceResponse.model_validate(data)
    result.id = str(result.id)

    return CommonResponse.success(data=result)


async def get_all(userId: str, db: AsyncSession) -> CommonResponse[SpaceListResponse]:
    data = await db.scalars(select(Space).where(Space.userId == int(userId)))
    results = data.all()
    results = [SpaceResponse.model_validate(row) for row in results]
    
    for result in results:
        result.id = str(result.id)

    return CommonResponse.success(data=SpaceListResponse(spaceList=results))


# in theory it should be in node service
async def get_nodes_by_space(spaceId: str, db: AsyncSession):
    result = await db.scalars(
        select(Node)
        .join(NodesRelations, Node.id == NodesRelations.nodeId)
        .where(NodesRelations.spaceId == int(spaceId))
    )
    return result.all()