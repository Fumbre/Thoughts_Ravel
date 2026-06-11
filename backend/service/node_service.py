from sqlalchemy import select
# from request.space_request import SpaceRequest, SpaceListRequest
from decorators.decor import Transactional
from model.node import Nodes
from common.db.session import AsyncSession
from common.response.default import CommonResponse
from common.id.snowflake_id_util import getId

# from service.node_service import insert as node_insert
from request.node_request import NodeSpaceListRequest, NodeSpaceRequest
from response.node_response import NodeResponse, NodeListResponse
from response.user_response import UserResponse
from common.filter.user import get_current_user
from fastapi import Request



@Transactional
async def insert(request: NodeSpaceListRequest, db: AsyncSession, req: Request) -> CommonResponse[NodeListResponse]:
    nodeSpace: NodeSpaceRequest = request.nodeSpaceList[0]

    user = get_current_user(req)

    ancestor = '0'

    nodeSpaceList: NodeListResponse =  []

    if nodeSpace.parent_id != 0: 
        node_orm = await db.scalar(select(Nodes).where(Nodes.id == nodeSpace.parent_id))
        node = NodeResponse.model_validate(node_orm)
        ancestor = f"{node.ancestor },{nodeSpace.parent_id}"
        position_x = node.position_x - 50
        position_y = node.position_y + 50

    for nodeSpaceItem in request.nodeSpaceList:
        id = getId()
        nodeSpaceItem = Nodes(**nodeSpaceItem.model_dump())
        nodeSpaceItem.id = id
        nodeSpaceItem.creater_id = user["id"]
        nodeSpaceItem.ancestor = ancestor
        nodeSpaceItem.position_x = position_x or nodeSpaceItem.position_x
        nodeSpaceItem.position_y = position_y or nodeSpaceItem.position_y

        nodeSpaceList.append(nodeSpaceItem)

    db.add_all(nodeSpaceList)

    return CommonResponse.success(data=nodeSpaceList)
       

async def get_user_nodes_by_parent(request: Request, parent_id: int, db: AsyncSession) -> CommonResponse[NodeListResponse]:
    user: UserResponse = get_current_user(request)

    data = await db.scalars(select(Nodes).where(Nodes.creater_id == user["id"], Nodes.parent_id == parent_id))
    results = data.all()

    results = [NodeResponse.model_validate(row) for row in results]

    for result in results:
        result.id = str(result.id)
        result.parent_id = str(result.parent_id)

    return CommonResponse.success(data=NodeListResponse(nodeList=results))


async def get_user_node(request: Request, node_id: int, db: AsyncSession) -> NodeResponse:
    user: UserResponse = get_current_user(request)

    data = await db.scalar(select(Nodes).where(Nodes.id == node_id, Nodes.creater_id == user["id"]))

    result = NodeResponse.model_validate(data)

    # fix snoflik id for frontend
    result.id = str(result.id)
    result.parent_id = str(result.parent_id)

    return CommonResponse.success(data=result)





# async def get_all(userId: str, db: AsyncSession) -> CommonResponse[SpaceListResponse]:
#     data = await db.scalars(select(Space).where(Space.userId == int(userId)))
#     results = data.all()
#     results = [SpaceResponse.model_validate(row) for row in results]
    
#     for result in results:
#         result.id = str(result.id)

#     return CommonResponse.success(data=SpaceListResponse(spaceList=results))


# # in theory it should be in node service
# async def get_nodes_by_space(spaceId: str, db: AsyncSession):
#     result = await db.scalars(
#         select(Node)
#         .join(NodesRelations, Node.id == NodesRelations.nodeId)
#         .where(NodesRelations.spaceId == int(spaceId))
#     )
#     return result.all()