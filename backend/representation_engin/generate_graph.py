import networkx as nx
from response.node_response import NodeResponse, NodeListResponse
from response.node_correlations_response import NodeCorrelationsListResponse

def generate_graph(root: NodeResponse, nodes: NodeListResponse, correlations: NodeCorrelationsListResponse):
    # Initialize NetworkX Directed Graph
    G = nx.DiGraph()
    
    # Add root node with full layout properties
    G.add_node(
        str(root.id), 
        label=root.name, 
        color=root.color, 
        shape=root.shape,
        x=root.position_x,
        y=root.position_y
    )
    
    # Add all child nodes
    for node in (nodes.nodeList or []):
        G.add_node(
            str(node.id), 
            label=node.name, 
            color=node.color, 
            shape=node.shape,
            x=node.position_x,
            y=node.position_y
        )
    
    # Inject edges from correlations list
    if len(correlations) > 0:
        for rel in (correlations.nodeCorrelationsList or []):

            # Check to avoid isolated edge crashes if a reference node is missing
            if G.has_node(rel.parent_node_id) and G.has_node(rel.destination_node_id):
                G.add_edge(rel.parent_node_id, rel.destination_node_id, label=rel.name)
            
    # Transform NetworkX structure directly to front-end ready dictionaries
    vis_nodes = []
    for node_id, data in G.nodes(data=True):
        vis_nodes.append({
            "id": node_id,
            "label": data.get("label"),
            "color": data.get("color"),
            "shape": data.get("shape"),
            "x": data.get("x"),
            "y": data.get("y")
        })
        
    vis_edges = []
    
    for source, target, data in G.edges(data=True):
        vis_edges.append({
            "from": source,
            "to": target,
            "label": data.get("label")
        })
        
    return {"nodes": vis_nodes, "edges": vis_edges}