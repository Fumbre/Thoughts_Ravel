from sqlalchemy import select
from request.space_request import SpaceRequest, SpaceListRequest
from decorators.decor import Transactional
from model.space import Space
from model.node import Node, NodesRelations
from common.db.session import AsyncSession
from common.response.default import CommonResponse
from common.id.snowflake_id_util import getId

from service.node_service import insert as node_insert

from response.space_response import SpaceResponse, SpaceListResponse

CURRENT_USER = 1

@Transactional
async def insert(request: SpaceListRequest, db: AsyncSession) -> CommonResponse:
    emptySpaceList = []
    emptyNodeList = []
    emptyNodeRelationList = []

    for space in request.spaceList :
        spaceId = getId()
        nodeId = getId()

        orm_space = Space(**space.model_dump())
        orm_space.id = spaceId

        # orm_node = Node(**node.model_dump())
        node = Node(
            id=nodeId,
            name=orm_space.title,
            positionX= 0,
            positionY= 0,
            color='blue',
            shape='circle',
            creater_id=CURRENT_USER
        )

        nodesRelations = NodesRelations(
            parentId = 0,
            nodeId = nodeId,
            spaceId = spaceId,
            userId = CURRENT_USER,
            public_status = 'r'
        )

        emptyNodeList.append(node)
        emptyNodeRelationList.append(nodesRelations)
        emptySpaceList.append(orm_space)

    db.add_all(emptySpaceList)
    db.add_all(emptyNodeList)
    db.add_all(emptyNodeRelationList)

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


