# Importing dependencies
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import math

# To generate graph with random vertices
G = nx.lollipop_graph(4, 0)

# Creating a direct graph
G = nx.DiGraph()

adjMatrix = np.array([[math.inf, -5, 2, 3], [math.inf, math.inf, 4, math.inf], [math.inf, math.inf, math.inf, 1], [math.inf, math.inf, math.inf, math.inf]])
length = len(adjMatrix)

# Adding edges to graph
for i in range(length):
    for j in range(length):

        G.add_edge(i, j, weight=adjMatrix[i, j])
        print(adjMatrix[i, j])

# Retrieving position of nodes
pos = nx.random_layout(G)

# Drawing the finalised graph
nx.draw(G, pos, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()