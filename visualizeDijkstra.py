"""Code to visualize Djikstra Table form output"""

# Importing dependencies
import visualize as vis
import numpy as np 
import math


def convert(mainTable, iteration):

   """Using this function to create adjacency matrices of shortest 
   paths from all vertices (as source) returned by main JohnsonsAlgorithm program"""

    num = len(mainTable)
    adjMatrix = np.full([num, num], math.inf)

    # Since we send the table (mainTable) a table which consists of 
    # solution for the computed graph using Dijkstras
    # Creating adjacency matrix from main table returned by JohnsonsAlgorithm program
    for j, i  in enumerate(mainTable):

        parent = i[1]
        distance = i[0]

        if parent == None:
            continue

        adjMatrix[parent, j] = distance - mainTable[parent][0]

    #print(mainTable)
    #print(adjMatrix)

    # Sending to adjacency matric to visualize.py to create/save graphs as per the iteration
    location="../Johnsons-Algorithm/static/images/soln{0}.png".format(iteration)
    vis.build_graph(num,adjMatrix,location)
