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
  net.save_graph("../nodes_ui.html")
  print("Файл успешно создан: nodes_ui.html")
except Exception as e:
  print(f"Ошибка: {e}")

# plt
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800)
plt.show()
