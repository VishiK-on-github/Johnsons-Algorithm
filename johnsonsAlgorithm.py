"""Code for the implementation of Johnson's Algorithm"""

# Importing dependencies
import numpy as np
import math

def ExtractMin(Q, mainTable):

    """Gives vertex in Q (Unvisited Set) minimum distance value"""

    minD = math.inf
    minE = None

    for i in Q:
        if mainTable[i][0] < minD:

            minD = mainTable[i][0]
            minE = i

    return minE

def adj(u, AdjMatrix):

    """Gives elements adjacent to current vertex"""

    AdjList = []

    for i in range(0, len(AdjMatrix[u])):

        if AdjMatrix[u][i] >= 0:

            AdjList.append(i)

    return AdjList

def Dijkstra(graph, source):

    """Code for implementing Dijkstra's Algorithm"""

    # Storing number of vertices
    numVertices = len(graph)

    # Table to store computed vertices
    mainTable = []
    Q = set()

    for v in range(0, numVertices):

        mTow = []
        Q.add(v)

        # Storing distance
        mTow.append(math.inf)
        # Parent
        mTow.append(None)

        # Adding the entity to Dijkstra's table
        mainTable.append(mTow)

    # Setting of source
    mainTable[source][0] = 0
    mainTable[source][1] = None

    # Repeating till visited set is empty
    while len(Q) != 0:

        u = ExtractMin(Q, mainTable)
        if u == None:
            break
        Q.remove(u)
        for v in adj(u, graph):
            if v in Q and mainTable[v][0] > mainTable[u][0] + graph[u, v]:
                    mainTable[v][0] = mainTable[u][0] + graph[u, v]
                    mainTable[v][1] = u


    # Returning the table to after graph Dijkstars ran sucessfully 
    #return mainTable
    print(mainTable)

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
    newGraph = np.zeros([len(graph), len(graph)])

    for i in range(len(graph)):
        for j in range(len(graph)):

            if graph[i, j] != 0:

                newGraph[i, j] = graph[i, j] + reweightFactor[i] - reweightFactor[j]

    # Non-negative weighted graph output
    #print("New Graph : ", newGraph)

    # Running Djiktras Algorithm by taking each of the vertices as source vertex
    for source in range(len(graph)):
        # Displaying method
        Dijkstra(newGraph, source)

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
    graph = np.array([[math.inf,3,8,math.inf,-4], [math.inf,math.inf,math.inf,1,7], [math.inf,4,math.inf,math.inf,math.inf], [2,math.inf,-5,math.inf,math.inf], [math.inf,math.inf,math.inf,6,math.inf]])

    # Calling the Johnsons method
    Johnson(graph)

if __name__ == "__main__":
    main()