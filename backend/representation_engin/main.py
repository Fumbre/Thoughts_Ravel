import networkx as nx
from pyvis.network import Network


# html
def generate_graph():
  G = nx.Graph()
  G.add_edge("A", "B")

  G.add_edge("B", "Ab")
  G.add_edge("B", "Bb")
  G.add_edge("B", "Cb")


  G.add_edge("A", "C")
  G.add_edge("C", "Aa") 
  G.add_edge("C", "Ba")

  G.add_edge("D", "Ab")
  G.add_edge("D", "Bb")
  G.add_edge("D", "Cb")


  net = Network(notebook=False, directed=False)

  net.from_nx(G)

  return {"nodes": net.nodes, "edges": net.edges}

# net = Network(notebook=False, directed=False)
# net.from_nx(G)

# try:
#   # nodes UI as index.html for node
#   net.save_graph("../index.html")
#   print("File created: index.html")
# except Exception as e:
#   print(f"Error: {e}")


