# controller/graph_render.py
from fastapi.routing import APIRouter
from fastapi import Depends
from common.db.session import DB, AsyncSession
from representation_engin.main import generate_graph
from service.node_relations_service import get as get_node_relations
# from service.node_service import get as get_node
from common.response.default import CommonResponse
from service.space_service import get as get_space, get_nodes_by_space

router = APIRouter(prefix='/api')

CURRENT_USER_ID = "1"  # mock, replace with JWT later

@router.get("/graph/{spaceId}")
async def get_graph(spaceId: str, db: AsyncSession = Depends(DB.get_session)) -> CommonResponse:
    relations = await get_node_relations(spaceId=spaceId, db=db)
    space = await get_space(id=spaceId, userId=CURRENT_USER_ID, db=db)
    nodes = await get_nodes_by_space(spaceId=spaceId, db=db)
    
    graph_data = generate_graph(
        relations.data,
        nodes_map=nodes,
        space_title=space.data.title
    )
    return CommonResponse.success(data=graph_data)