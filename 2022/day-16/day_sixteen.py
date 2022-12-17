from collections import deque
import re
import os
import sys
from time import sleep as wait


# get input
def get_input(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as f:
        input = f.read().splitlines()
        flows = [re.findall(r"(\d+)", line) for line in input]
        valves = [re.findall(r"([A-Z]{2})", line) for line in input]
        valve = [line[0] for line in valves]
        children = [line[1:] for line in valves]

    return flows, valve, children


# Valve object
class Valve(object):
    def __init__(self, name, flowRate, children):
        self.name = name
        self.flowRate = int(flowRate[0])
        self.children = children
        self.open = False
        self.dist = []

    def open(self):
        self.open = True

    def addDist(self, valveKey, flowRate, dist):
        self.dist.append((valveKey, flowRate, dist))


# parse input
def parse_input(flows, valve, children):
    graph = {}

    for i, line in enumerate(valve):
        graph[valve[i]] = Valve(valve[i], flows[i], children[i])
    return graph


# dijkstra algorithm to find max pressure path
# def dijkstra(graph, start):
#     time = 30


# find distances of all nonzero valves to other nonzero valves using BFS
def bfs(graph, valveStart):
    visited = []
    queue = deque([(valveStart, 0)])

    while queue:
        valve, dist = queue.popleft()
        if valve in visited:
            continue

        # and valve != valveStart:
        if graph[valve].flowRate > 0 and valve not in visited:
            graph[valveStart].dist.append(
                (valve, graph[valve].flowRate, dist + 1))  # added plus one to distance here to account for opening

        visited.append(valve)
        for child in graph[valve].children:
            queue.append((child, dist + 1))


# Using the distances find max pressure path in 30 min
# def find_max(paths, time):
#     for path in paths:
#         if (time - path[3] < 30):
#             return
#         else:
#             time -= path[3]
#             find_max(graph(path[0]).dist, time)


def find_paths(graph, valveStart):
    paths = [0]  # all of the paths
    pressures = [0]  # all of the pressures of the paths
    q = deque([(valveStart, [], 0, 0, 30)])
    maxPressure = 0

    while q:
        curr, path, pressure, pressureRelease, time = q.popleft()
        #print("Current: ", curr)
        # if curr in path:
        #     continue

        for child in graph[curr].dist:
            # wait(.5)
            if child[0] in path:
                print(len(q))

                if (pressure + (pressureRelease * (time-1))) > maxPressure and (pressure + (pressureRelease * (time-1))) < 1929:
                    # paths.pop(0)
                    # pressures.pop(0)
                    paths.append((curr, path, pressure, pressureRelease, time))
                    pressures.append(pressure + (pressureRelease * (time-1)))
                    # Issue with this time - 1
                    maxPressure = pressure + (pressureRelease * (time-1))
                print("MAX PRESSURE: ", maxPressure)
                print("PATH: ", paths)

                continue

            #print("CHILD", child)
            childPath = [*path]
            childPressure = pressure
            childPressureRelease = pressureRelease

            # if len(path) == (len(graph[valveStart].dist) + 1):
            #     paths.append((curr, path, pressure, pressureRelease, time))
            #     pressures.append(pressure + (pressureRelease * (time-1)))
            #     continue

            childPath.append(child[0])
            # dont multiple child pressure, multiple
            childPressure += child[1] + (childPressureRelease * (child[2]))
            childPressureRelease += child[1]

            # if len(path) == (len(graph[valveStart].dist) + 1):
            #     paths.append((curr, path, pressure, pressureRelease, time))
            #     pressures.append(pressure + (pressureRelease * (time-1)))
            #     print('hi')
            #     continue

            q.append((child[0], childPath, childPressure,
                      childPressureRelease, time - (child[2])))
            # print(q)

    return paths, pressures


# main function
def main(filename):
    flows, valve, children = get_input(filename)
    graph = parse_input(flows, valve, children)

    # run bfs and get distances to all nonzero flowrate
    for valveStart in valve:
        print(valveStart)
        if graph[valveStart].flowRate > 0 or valveStart == valve[0]:
            bfs(graph, valveStart)
            print(graph[valveStart].dist)

    # get all the paths starting from A that can be done in less than 30
    # print(graph.keys())
    paths, pressures = find_paths(graph, valve[0])

    print(paths)
    print(pressures)
    maxIndex = pressures.index(max(pressures))
    print(paths[maxIndex])
    print(pressures[maxIndex])
    #print(1651 in pressures)
    # path = deque([valve[0]])
    # while path:
    #     valve = path.popleft()

    # paths = []
    # for valve in graph[valve[0]].dist:
    #     time = 30
    #     time -= valve[3]
    #     path = []
    #     while time > 0:
    #         return 0


# 1849 too low
# 1908 too low
# 2016 too high


#1908, 2016, 1992, 1941
# 1992 not the right answer, neither 1941, 1935, 1930, 1929, 1927
main("input.txt")
