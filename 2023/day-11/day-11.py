import os
import sys
import re
import networkx as nx
import numpy as np


def manhattan_distance(p1, p2):
    """Calculates the Manhattan distance between two points.

    Args:
      p1: A list of two numbers representing the coordinates of the first point.
      p2: A list of two numbers representing the coordinates of the second point.

    Returns:
      The Manhattan distance between the two points.
    """

    return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

expandedNum = 999999
array = []
expandedRows = []
for i in range(0, len(results)):
    array.append(list(results[i]))

    if results[i].count(".") == len(results[i]):
        expandedRows.append(i)
        # for k in range(0, expandedNum):
        #     # print(k)
        #     array.append(list(results[i]))

# for arrayLine in array:
#     print(arrayLine)

expandCols = []
galaxyNum = 0
for i in range(0, len(array[0])):
    expand = 1
    for j in range(0, len(array)):
        if array[j][i] == ".":
            continue
        elif array[j][i] == "#":
            array[j][i] = galaxyNum
            galaxyNum += 1
            expand = 0
    # print(expand)
    if expand == 1:
        expandCols.append(i)


# for j in range(0, len(expandCols)):
#     for i in range(0, len(array)):
#         for k in range(0, expandedNum):
#             # print("expand col", k)
#             array[i].insert(expandCols[j] + (j * expandedNum), ".")


galaxyCoords = []
for i in range(0, len(array[0])):
    for j in range(0, len(array)):
        if array[j][i] == ".":
            continue
        else:
            galaxyCoords.append((j, i))
# print(galaxyCoords)
# for arrayLine in array:
#     print(arrayLine)

# print(len(array[0]), len(array))
G = nx.grid_2d_graph(len(array), len(array[0]))
# print(G)
sum = 0
print(len(galaxyCoords))
print(galaxyCoords)
for i in range(0, len(galaxyCoords)):
    print(i)
    for j in range(i + 1, len(galaxyCoords)):
        # print(sum)
        sum += manhattan_distance(galaxyCoords[i], galaxyCoords[j])
        for row in expandedRows:
            if (
                min(galaxyCoords[i][0], galaxyCoords[j][0])
                <= row
                <= max(galaxyCoords[i][0], galaxyCoords[j][0])
            ):
                sum += expandedNum
        for col in expandCols:
            if (
                min(galaxyCoords[i][1], galaxyCoords[j][1])
                <= col
                <= max(galaxyCoords[i][1], galaxyCoords[j][1])
            ):
                sum += expandedNum
        # sum += (
        #     len(
        #         nx.bidirectional_shortest_path(
        #             G, source=galaxyCoords[i], target=galaxyCoords[j]
        #         )
        #     )
        #     - 1
        # )
print(sum)
# run dijkstra on each galaxy to get pair with each other and then remove galaxy
