import networkx as nx
from pyvis.network import Network
from response.node_relations_response import NodeRelationsListResponse


# object
def generate_graph(data: NodeRelationsListResponse, nodes_map: list, space_title: str = "root"):
    nodes_dict = {str(n.id): n for n in nodes_map}
    
    G = nx.Graph()
    for relation in data.nodeRelationsList:
        G.add_edge(str(relation.parentId), str(relation.nodeId))
    
    G.remove_node('0')  

    net = Network(notebook=False, directed=False)
    net.from_nx(G)
    
    for node in net.nodes:
        if node['id'] == '0':
            node['label'] = space_title
        else:
            n = nodes_dict.get(str(node['id']))
            if n:
                node['label'] = n.name
                node['color'] = n.color
    
    return {"nodes": net.nodes, "edges": net.edges}

