from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from fastapi import Depends, Request, Response
from request.node_request import NodeSpaceListRequest, NodeEdgeListRequest, NodeSpaceRequest, NodePositionUpdateRequest
from service.node_service import insert, get_user_nodes_by_parent, get_user_node, make_node_edge, update_position


router = APIRouter(prefix='/api')


@router.get('/node/{node_id}')
async def getUserNode(request: Request, node_id: str ,db:AsyncSession = Depends(DB.get_session)) -> CommonResponse:
    return await get_user_node(request = request, db = db, node_id = int(node_id))

@router.patch('/node')
async def updateNodePos(body: NodePositionUpdateRequest)-> CommonResponse:
    return await update_position(
        node_id=int(body.id), 
        position_x=body.position_x, 
        position_y=body.position_y, 
    )


@router.post('/node')
async def postNodeEdge(request: Request, body: NodeEdgeListRequest) -> str:
    mapped_space_nodes = []
    
    for edge in (body.nodeEdgeList or []):  # Use the exact list field name from your request model
        space_node = NodeSpaceRequest(
            name=edge.name,
            parent_id=edge.space_id,
            description=edge.description,
            type=edge.type,
            shape=edge.shape,
            color=edge.color,
            position_x=0.0,
            position_y=0.0
        )
        mapped_space_nodes.append(space_node)

    space_list_payload = NodeSpaceListRequest(nodeSpaceList=mapped_space_nodes)

    created_nodes = await insert(request=space_list_payload, req=request)
    if created_nodes.code != 200:
        return CommonResponse.faild()
    
    result = await make_node_edge(created_nodes.data, body)

    print("finale,")
    return "return result for updating reactivly"

@router.post('/space')
async def createNodeSpace(request: Request, body: NodeSpaceListRequest) -> CommonResponse:
    return await insert(request = body, req = request)

@router.get('/space')
async def getUserNodesSpaces(request: Request, parent_id: str ,db:AsyncSession = Depends(DB.get_session)) -> CommonResponse:
    return await get_user_nodes_by_parent(request = request, db = db, parent_id=int(parent_id))