from sqlalchemy import select, and_, update, func
# from request.space_request import SpaceRequest, SpaceListRequest
from decorators.decor import Transactional
from model.node import Nodes
from model.node_correlation import NodeCorrelations
from common.db.session import AsyncSession
from common.response.default import CommonResponse
from common.id.snowflake_id_util import getId

# from service.node_service import insert as node_insert
from request.node_request import NodeSpaceListRequest, NodeSpaceRequest, NodeEdgeListRequest
from response.node_response import NodeResponse, NodeListResponse
from response.user_response import UserResponse
from response.node_correlations_response import NodeCorrelationsListResponse, NodeCorrelationResponse
from common.filter.user import get_current_user
from fastapi import Request


@Transactional
async def insert(request: NodeSpaceListRequest, db: AsyncSession, req: Request = None, user_id: int = None) -> CommonResponse[NodeListResponse]:
    nodeSpace: NodeSpaceRequest = request.nodeSpaceList[0]

    if user_id is None:
        user = get_current_user(req)
        user_id = user["id"]

    ancestor = '0'

    nodeSpaceList: NodeListResponse =  []

    if nodeSpace.parent_id != 0: 
        node_orm = await db.scalar(select(Nodes).where(Nodes.id == nodeSpace.parent_id))
        node = NodeResponse.model_validate(node_orm)
        ancestor = f"{node.ancestor },{nodeSpace.parent_id}"
        # position_x = node.position_x - 50
        # position_y = node.position_y + 50

    for nodeSpaceItem in request.nodeSpaceList:
        id = getId()
        nodeSpaceItem = Nodes(**nodeSpaceItem.model_dump())
        nodeSpaceItem.id = id
        nodeSpaceItem.creater_id = user_id
        nodeSpaceItem.ancestor = ancestor
        # nodeSpaceItem.position_x = position_x or nodeSpaceItem.position_x
        # nodeSpaceItem.position_y = position_y or nodeSpaceItem.position_y

        nodeSpaceList.append(nodeSpaceItem)

    db.add_all(nodeSpaceList)

    validated_nodes = [NodeResponse.model_validate(item) for item in nodeSpaceList]
    response_payload = NodeListResponse(nodeList=validated_nodes)

    return CommonResponse.success(data=response_payload)
       

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

async def get_user_nodes(user_id: int, db: AsyncSession) -> CommonResponse:

    result = await db.scalar(
        select(func.count(Nodes.id)).where(Nodes.creater_id == user_id)
    )
    
    # Fallback to 0 if the query somehow returns None
    count_value = result or 0

    return CommonResponse.success(data=count_value)

@Transactional
async def make_node_edge(nodes: NodeListResponse, edges: NodeEdgeListRequest, db: AsyncSession) -> CommonResponse:
    correlations_to_add = [
        NodeCorrelations(
            parent_node_id=edge.parent_node_id,
            destination_node_id=node.id,
            name=edge.label
        )   
        for node in (nodes.nodeList or [])
        for edge in (edges.nodeEdgeList or [])
    ]

    if correlations_to_add:
        db.add_all(correlations_to_add)
        await db.flush()

    result = [
    {
        "id": str(node.id),
        "name": node.name,
        "color": node.color,
        "shape": node.shape,
        "position_x": node.position_x,
        "position_y": node.position_y,
        "parent_node_id": str(edge.parent_node_id), 
    }
    for node, edge in zip(nodes.nodeList or [], edges.nodeEdgeList or [])
]

    print("bla bla",result)

    return CommonResponse.success(data=result)


async def get_node_correlation(root_id: str, nodes: NodeListResponse, db: AsyncSession) -> CommonResponse[NodeCorrelationsListResponse]:
    # Start with the root space ID itself
    visible_node_ids = {int(root_id)}
    
    # Add every child node ID from your pre-fetched list
    for node in (nodes.nodeList or []):
        visible_node_ids.add(node.id)

    # Safety check: If there are no nodes at all, don't hit the DB
    if not visible_node_ids:
        return NodeCorrelationsListResponse(nodeCorrelationsList=[])

    stmt = select(NodeCorrelations).where(
        and_(
            NodeCorrelations.parent_node_id.in_(visible_node_ids),
            NodeCorrelations.destination_node_id.in_(visible_node_ids)
        )
    )
    
    # Execute the query asynchronously
    result = await db.scalars(stmt)
    correlations_orm = result.all()
    
    # Serialize  database rows directly into Pydantic schema layout
    validated_correlations = [
        NodeCorrelationResponse.model_validate(c) for c in correlations_orm
    ]

    return CommonResponse.success(data=NodeCorrelationsListResponse(nodeCorrelationsList=validated_correlations))


@Transactional
async def update_position(node_id: int, position_x: float, position_y: float, db: AsyncSession) -> CommonResponse:
    stmt = (
        update(Nodes)
        .where(Nodes.id == node_id)
        .values(position_x=position_x, position_y=position_y)
    )
    
    await db.execute(stmt)
    return CommonResponse.success(message="Node coordinates successfully updated")