from collections import deque
import re
import os
import sys
from time import sleep as wait


# get input (Put ints into flows and all uppercase two letters into valves then split into valve + children)
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
        self.dist = []

    def addDist(self, valveKey, flowRate, dist):
        self.dist.append((valveKey, flowRate, dist))


# parse input
def parse_input(flows, valve, children):
    graph = {}

    for i, line in enumerate(valve):
        graph[valve[i]] = Valve(valve[i], flows[i], children[i])
    return graph


# find distances of all nonzero valves to other nonzero valves using BFS
def bfs(graph, valveStart):
    visited = []
    queue = deque([(valveStart, 0)])

    while queue:
        valve, dist = queue.popleft()
        if valve in visited:
            continue

        if graph[valve].flowRate > 0 and valve not in visited:
            graph[valveStart].dist.append(
                (valve, graph[valve].flowRate, dist + 1))  # added plus one to distance here to account for opening

        visited.append(valve)
        for child in graph[valve].children:
            queue.append((child, dist + 1))


# Another bfs to get all paths and pressures, keeping track of maxpressure when child of curr is in path
# This does all the math of deleting from totalTime the distance plus opening of valve
def find_paths(graph, valveStart, totalTime):
    paths = [0]  # all of the paths
    pressures = [0]  # all of the pressures of the paths
    q = deque([(valveStart, [], 0, 0, totalTime)])
    maxPressure = 0

    while q:
        curr, path, pressure, pressureRelease, time = q.popleft()

        for child in graph[curr].dist:
            if child[0] in path:
                if (pressure + (pressureRelease * (time-1))) > maxPressure and (pressure + (pressureRelease * (time-1))) < 1929:
                    paths.pop(0)
                    pressures.pop(0)
                    paths.append((curr, path, pressure, pressureRelease, time))
                    pressures.append(pressure + (pressureRelease * (time-1)))
                    maxPressure = pressure + (pressureRelease * (time-1))
                continue

            childPath = [*path]
            childPressure = pressure
            childPressureRelease = pressureRelease

            childPath.append(child[0])
            # dont multiple child pressure, multiple
            childPressure += child[1] + (childPressureRelease * (child[2]))
            childPressureRelease += child[1]

            if time - child[2] < 0:
                continue

            q.append((child[0], childPath, childPressure,
                      childPressureRelease, time - (child[2])))

    return paths, pressures


# main function
def main(filename):

    # -------------------------------------------------------------------------------------------------
    # PART 1
    flows, valve, children = get_input(filename)
    graph = parse_input(flows, valve, children)

    startIndex = 0
    for i, valveStart in enumerate(valve):
        if valveStart == 'AA':
            startIndex = i

    # run bfs and get distances to all nonzero flowrate
    for valveStart in valve:
        if graph[valveStart].flowRate > 0 or valveStart == valve[startIndex]:
            bfs(graph, valveStart)

    # get all the paths starting from A that can be done in less than 30
    paths, pressures = find_paths(graph, valve[startIndex], 30)

    print(paths[0])
    print(pressures[0])

    # -------------------------------------------------------------------------------------------------
    # PART 2
    # run part 1 with 26 minutes, and then turn that top path's valves to 0 and run again with new valves
    print("PART 2")

    # Part 1 with 26 minutes
    flows, valve, children = get_input(filename)
    graph = parse_input(flows, valve, children)

    startIndex = 0
    for i, valveStart in enumerate(valve):
        if valveStart == 'AA':
            startIndex = i

    for valveStart in valve:
        if graph[valveStart].flowRate > 0 or valveStart == valve[startIndex]:
            bfs(graph, valveStart)

    paths1, pressures1 = find_paths(graph, valve[startIndex], 26)

    # Part 1 with 26 minutes and the optimal human valves opened set to zero to find optimal elephant
    print(paths1[0])
    print(pressures1[0])

    for valve in paths1[0][1]:
        graph[valve].flowRate = 0

    flows, valve, children = get_input(filename)
    graph = parse_input(flows, valve, children)

    for valve1 in paths1[0][1]:
        graph[valve1].flowRate = 0

    for valveStart in valve:
        if graph[valveStart].flowRate > 0 or valveStart == valve[startIndex]:
            bfs(graph, valveStart)

    paths2, pressures2 = find_paths(graph, valve[startIndex], 26)
    print(paths2[0])
    print(pressures2[0])

    # add optimal human and optimal leftover elphant to get maxpressure
    print(pressures1[0] + pressures2[0])


main("input.txt")
