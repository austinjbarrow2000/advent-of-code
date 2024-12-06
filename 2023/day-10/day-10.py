import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


def get_neighbors(node, grid):
    neighbors = []
    # up
    if node[0] > 0 and grid[node[0] - 1][node[1]] != "#":
        neighbors.append((node[0] - 1, node[1], "up"))
    # down
    if node[0] < len(grid) - 1 and grid[node[0] + 1][node[1]] != "#":
        neighbors.append((node[0] + 1, node[1], "down"))
    # left
    if node[1] > 0 and grid[node[0]][node[1] - 1] != "#":
        neighbors.append((node[0], node[1] - 1, "left"))
    # right
    if node[1] < len(grid[0]) - 1 and grid[node[0]][node[1] + 1] != "#":
        neighbors.append((node[0], node[1] + 1, "right"))
    return neighbors


def mark_visited(node, path, v):
    v[(node[0], node[1])] = len(path)


def is_visited(node, v):
    return v[(node[0], node[1])]


def can_traverse(grid, node, item):
    if grid(node[0], node[1]) == "S" and grid(item[0], item[1]) != ".":
        return True
        # elif (
        #     grid(node[0], node[1]) == "-"
        #     and grid(item[0], item[1]) != "."
        #     and (item[2] == "left" or item[2] == "right")
        # ):
        #     return True
        # elif (
        #     grid(node[0], node[1]) == "|"
        #     and grid(item[0], item[1]) != "."
        #     and (item[2] == "left" or item[2] == "right")
        # ):
        return True

    return True


def find_path_bfs(s, grid, v):
    queue = [(s, [])]  # start point, empty path

    while len(queue) > 0:
        node, path = queue.pop(0)
        path.append(node)
        mark_visited(node, path, v)
        distance += 1

        # if node == e:
        #     return path

        adj_nodes = get_neighbors(node, grid)
        for item in adj_nodes:
            if not is_visited(item, v) and can_traverse(grid, node, item):
                queue.append((item, path[:]))

    # return None  # no path found


filename = "./input.txt"
results = get_input(filename)

map = []
for i in range(0, len(results)):
    map.append(list(results[i]))
    if "S" in results[i]:
        start = (i, results[i].index("S"))

visited = {}

find_path_bfs(start, map, visited)

print(max(visited.values()))
