# get input function
import os
import sys
import numpy as np


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        input = f.read().strip()
    return input


def parse_input(input):
    grid = [list(line) for line in input.split("\n")]
    start = end = None
    a_list = []

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == "S":
                start = (i, j)
                a_list.append(start)
                grid[i][j] = "a"
            elif val == "E":
                end = (i, j)
                grid[i][j] = "z"
            elif val == "a":
                a_list.append((i, j))
    return grid, start, end, a_list


# def get_neighbors(indices, array):
#     x = indices[0]
#     y = indices[1]
#     neighbors = []

#     if x - 1 >= 0:
#         if ord(array[x - 1, y]) <= (ord(array[x, y]) + 1) or (
#             array[x - 1, y] == "E" and array[x, y] == "z"
#         ):
#             neighbors.append([x - 1, y])
#     if y - 1 >= 0:
#         if ord(array[x, y - 1]) <= (ord(array[x, y]) + 1) or (
#             array[x - 1, y] == "E" and array[x, y] == "z"
#         ):
#             neighbors.append([x, y - 1])
#     if x + 1 < array.shape[0]:
#         if ord(array[x + 1, y]) <= (ord(array[x, y]) + 1) or (
#             array[x - 1, y] == "E" and array[x, y] == "z"
#         ):
#             neighbors.append([x + 1, y])
#     if y + 1 < array.shape[1]:
#         if ord(array[x, y + 1]) <= (ord(array[x, y]) + 1) or (
#             array[x - 1, y] == "E" and array[x, y] == "z"
#         ):
#             neighbors.append([x, y + 1])
#     return neighbors


# breath first search for shortest path
# def bfs(array, start):
#     visited = []
#     queue = []
#     print(start)
#     print("hi")

#     visited.append(start)
#     queue.append(start)

#     while queue:
#         print(array[queue[0][0], queue[0][1]])
#         neighbors = get_neighbors(queue[0], array)
#         print(queue[0])
#         for neighbor in neighbors:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 visited.append(neighbor)
#                 if array[visited[-1][0], visited[-1][1]] == "E":
#                     return

#         queue.pop(0)

#     # print(visited)
#     # print(visited[-1])
#     # print(array[visited[-1][0], visited[-1][1]])

from collections import deque


def bfs(grid, starts, end):
    visited = []
    queue = deque([(start, 0) for start in starts])
    while queue:
        pos, dist = queue.popleft()
        if pos == end:
            return dist
        if pos in visited:
            continue

        visited.append(pos)
        x, y = pos
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):  # neighbors
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and ord(grid[x + dx][y + dy]) - ord(grid[x][y]) <= 1
            ):
                queue.append(((x + dx, y + dy), dist + 1))
    return None


def main(filename):
    input = get_input(filename)
    grid, start, end, a_list = parse_input(input)

    print(bfs(grid, [start], end))  # Part 1
    print(bfs(grid, a_list, end))  # Part 2


main("input.txt")
