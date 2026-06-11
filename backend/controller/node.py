from common.db.session import DB, AsyncSession
from fastapi.routing import APIRouter
from common.response.default import CommonResponse
from fastapi import Depends, Request, Response
from request.node_request import NodeSpaceListRequest, NodeEdgeListRequest, NodeSpaceRequest
from service.node_service import insert, get_user_nodes_by_parent, get_user_node


router = APIRouter(prefix='/api')


@router.get('/node/{node_id}')
async def getUserNode(request: Request, node_id: str ,db:AsyncSession = Depends(DB.get_session)) -> CommonResponse:
    return await get_user_node(request = request, db = db, node_id = int(node_id))

@router.post('/node')
async def postNodeEdge(request: Request, body: NodeEdgeListRequest) -> str:
    print("Incoming body:", body)

    mapped_space_nodes = []
    
    for edge in (body.nodeEdgeList or []):  # Use the exact list field name from your request model
        space_node = NodeSpaceRequest(
            name=edge.name,
            parent_id=edge.parent_id,
            description=edge.description,
            type=edge.type,
            shape=edge.shape,
            color=edge.color,
            position_x=0.0,
            position_y=0.0
        )
        mapped_space_nodes.append(space_node)

    space_list_payload = NodeSpaceListRequest(nodeSpaceList=mapped_space_nodes)

    test = await insert(request=space_list_payload, req=request)
    print("finale,",test)
    return ""

@router.post('/space')
async def createNodeSpace(request: Request, body: NodeSpaceListRequest) -> CommonResponse:
    return await insert(request = body, req = request)

@router.get('/space')
async def getUserNodesSpaces(request: Request, parent_id: str ,db:AsyncSession = Depends(DB.get_session)) -> CommonResponse:
    return await get_user_nodes_by_parent(request = request, db = db, parent_id=int(parent_id))