# Importing dependencies
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import math



def build_graph(n, adjMatrix, location):
    
    # Receieving number of vertices, adjacency matrix and location of where image has to be stored
    # To generate graph with random vertices layout
    G = nx.lollipop_graph(n, 0)


    

    # Creating a directed graph
    G = nx.DiGraph()


    """#Relabelling node names to alphabets
    mapping={}
    char=65
    for i in range(n):
        mapping[i]=chr(char)
        char+=1"""

    #adjMatrix = np.array([[math.inf, -5, 2, 3], [math.inf, math.inf, 4, math.inf], [math.inf, math.inf, math.inf, 1], [math.inf, math.inf, math.inf, math.inf]])
    length = len(adjMatrix)

    # Adding edges to graph
    for i in range(length):
        for j in range(length):

            if(adjMatrix[i,j] == math.inf):
                continue

            G.add_edge(i, j, weight=adjMatrix[i, j])
            #print(adjMatrix[i, j])

    # Retrieving position of nodes
    #pos = nx.random_layout(G)
    pos=nx.circular_layout(G)


   
   

    # Drawing the finalised graph
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    
  

    plt.savefig(location, format="PNG")
    # plt.show()
    plt.clf()