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

"""def update(mainTable, graph, u, Q):

    for v in adj(u, graph):
        if v in Q and mainTable[v][0] > mainTable[u][0] + graph[u, v]:
                mainTable[v][0] = mainTable[u][0] + graph[u, v]
                mainTable[v][1] = u

    return mainTable"""


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
    return mainTable