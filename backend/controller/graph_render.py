# controller/graph_render.py
from fastapi.routing import APIRouter
from fastapi import Depends
from common.db.session import DB, AsyncSession
from representation_engin.main import generate_graph
from service.node_relations_service import get as get_node_relations
from service.node_service import get as get_node
from service.space_service import get as get_space

router = APIRouter(prefix='/api')

@router.get("/graph/{spaceId}")
async def get_graph(spaceId: str, db: AsyncSession = Depends(DB.get_session)):
    relations = await get_node_relations(spaceId=spaceId, db=db)
    space = await get_space(id=spaceId, userId='1', db=db)

    
    nodesData = []
    # super bad approach, uses a lot of requests to db
    for relation in relations.data.nodeRelationsList:
        nodeData = await get_node(str(relation.nodeId), db=db)
        nodesData.append(nodeData.data)



    return generate_graph(relations.data, nodes_map=nodesData, space_title=space.data.title)
    