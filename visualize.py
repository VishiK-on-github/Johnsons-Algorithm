import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#To generate graph with random vertices
G = nx.lollipop_graph(4, 0)
#Creating a direct graph
G = nx.DiGraph()

adjMatrix = np.array([[0, -5, 2, 3], [0, 0, 4, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
length = len(adjMatrix)
#Adding edges to graph
for i in range(length):
    for j in range(length):
        if adjMatrix[i, j] != 0 and adjMatrix != math.inf:
            G.add_edge(i, j, weight=adjMatrix[i, j])

#Retrieving position of nodes
pos = nx.random_layout(G)

#Drawing the finalised graph
nx.draw(G,pos,with_labels=True,font_weight='bold')
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()