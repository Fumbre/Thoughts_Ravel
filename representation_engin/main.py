import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt

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

# html

net = Network(notebook=False, directed=False)
net.from_nx(G)

try:
  # nodes UI as index.html for node
  net.save_graph("../front/src/index.html")
  print("File created: index.html")
except Exception as e:
  print(f"Error: {e}")


