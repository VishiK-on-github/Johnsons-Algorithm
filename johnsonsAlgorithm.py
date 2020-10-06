"""Code for the implementation of Johnson's Algorithm"""

# Importing dependencies
import numpy as np
import math
from Testing import testDijkstra as td

# Code Done
def BellmanFord(edges, graph):

    """Code for running Bellman-Ford"""

    # To get number of vertices
    num =  len(graph)

    # Initializing a distance list
    dist = [math.inf] * (num + 1)

    # Distance from source to source will always be zero
    dist[num] = 0

    # Inserting edges from imaginary source to vertices in edge list
    for i in range(num):
        edges.append([num, i, 0])

    # Running Bellmanford loop, number of vertices times
    for i in range(num):
        for (source, destination, weight) in edges:
            
            if (dist[source] != math.inf) and (dist[source] + weight < dist[destination]):

                dist[destination] = dist[source] + weight

    # Returning reweighted graph
    return dist[0:num]

# Code done
def Johnson(graph):

    """Code for running Johnson's"""

    # Creating an empty list to store non-zero edges
    edges = []

    # Creating a list of non-zero edges to be sent to Bellmanford to be reweighted
    for i in range(len(graph)):
        for j in range(len(graph[i])):

            if graph[i, j] != 0:
                edges.append([i, j, graph[i, j]])

    # Modified weights returned by Bellmanford method
    reweightFactor = BellmanFord(edges, graph)

    # Creating an adjacency matrix with all entries as zero
    newGraph = np.zeros([len(graph), len(graph)], dtype=int)

    for i in range(len(graph)):
        for j in range(len(graph)):

            if graph[i, j] != 0:

                newGraph[i, j] = graph[i, j] + reweightFactor[i] - reweightFactor[j]

    # Non-negative weighted graph output
    print("New Graph : ", newGraph)

    # Running Djiktras Algorithm by taking each of the vertices as source vertex
    for source in range(len(graph)):
        # Displaying method
        td.Dijkstra(newGraph, source)

def main():

    """Driver Code"""

    # Dictionary to store names of the vertices
    """vertexIndex = {}

    # Enter the number of vertices
    numVertex = int(input("Enter the total number of vertices in the graph : "))

    # To get names of the vertices
    for i in range(0, numVertex):

        verName = input(f"Enter the name of {i + 1} vertex : ")
        vertexIndex[i] = verName"""

    # Testing adjacency matrix
    graph = np.array([[0, -5, 2, 3], [0, 0, 4, 0], [0, 0, 0, 1], [0, 0, 0, 0]])

    # To get the adjacency matrix
    """adjMatrix = np.zeros([numVertex, numVertex], dtype=int)"""

    # For building custom user input
    """for i in range(numVertex):
        for j in range(numVertex):

            if i != j:
                weight = int(input(f"Enter distance from {i} to {j} : "))
                adjMatrix[i, j] = weight"""


    # Calling the Johnsons method
    Johnson(graph)

if __name__ == "__main__":
    main()