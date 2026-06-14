from langchain_core.tools import tool
from common.filter.user import get_current_user
from service.node_service import get_user_nodes, insert, make_node_edge
from controller.node import postNodeEdge
from common.response.default import CommonResponse
from request.node_request import NodeEdgeListRequest, NodeEdgeRequest, NodeSpaceListRequest, NodeSpaceRequest
from common.db.session import DB 
import json

# Define tools for AI to use
@tool
async def get_nodes(user_id: str) -> CommonResponse:
    """
    Return counts of all nodes for the **user_id**
    DO NOT ANSWER WITH **user_id**
    """
    async for db in DB.get_session():
        result = await get_user_nodes(user_id=int(user_id), db=db)
        print(result)
        
        return CommonResponse.success(data=result)
    
@tool
async def create_nodes(user_id: str, root_node_id: str, node_names: str) -> str:
    """
    Create child nodes under root_node_id for the user.
    node_names is a comma separated list of names e.g. 'Node A, Node B, Node C'
    """
    names = [n.strip() for n in node_names.split(',')]

    edges = NodeEdgeListRequest(nodeEdgeList=[
        NodeEdgeRequest(
            name=name,
            space_id=root_node_id,
            parent_node_id=root_node_id,
            description='',
            type='0',
            shape='circle',
            color='blue',
            parent_pos_x=0,
            parent_pos_y=0,
            label=name,
        )
        for name in names
    ])

    mapped_nodes = [
        NodeSpaceRequest(
            name=edge.name,
            parent_id=int(edge.parent_node_id),
            description=edge.description,
            type=edge.type,
            shape=edge.shape,
            color=edge.color,
            position_x=edge.parent_pos_x - 50,
            position_y=edge.parent_pos_y + 50,
        )
        for edge in edges.nodeEdgeList
    ]
    space_payload = NodeSpaceListRequest(nodeSpaceList=mapped_nodes)

    # @Transactional handles its own db session 
    created = await insert(request=space_payload, user_id=int(user_id))
    if created.code != 200:
        return "Failed to create nodes"

    result = await make_node_edge(created.data, edges)
    return json.dumps(result.data)