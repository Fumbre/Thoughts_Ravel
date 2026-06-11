# controller/graph_render.py

from fastapi.routing import APIRouter
from fastapi import Depends, Request
from common.db.session import DB, AsyncSession
from common.response.default import CommonResponse
from representation_engin.generate_graph import generate_graph

# from service.node_service import get as get_node
# from service.node_relations_service import get as get_node_relations
# from service.space_service import get as get_space, get_nodes_by_space
from service.node_service import get_user_nodes_by_parent, get_user_node

router = APIRouter(prefix='/api')

@router.get("/graph/{space_id}")
async def get_graph(request: Request, space_id: str, db: AsyncSession = Depends(DB.get_session)) -> CommonResponse:
    root_node = await get_user_node(request=request, node_id=space_id, db=db)
    if root_node.code != 200:
        return CommonResponse.response(code=401, message="Node is not exists for this user")
        
    nodes = await get_user_nodes_by_parent(request= request, parent_id=int(space_id), db=db)

    if nodes.code != 200:
        return CommonResponse.response(code=401, message="Node is not exists for this user")

    root_node = root_node.data
    nodes = nodes.data
    

    # print(nodes)
    # print(root_node)
    
    graph_data = generate_graph(
        root=root_node,
        nodes=nodes,
        correlations=[]
    )

    return CommonResponse.success(data=graph_data)