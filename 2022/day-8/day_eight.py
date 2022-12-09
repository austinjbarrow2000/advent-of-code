import numpy as np

## Functions
import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


def check_visible(x, y, grid, value):
    left = grid[x, :y]
    right = grid[x, y + 1 : len(grid)]
    top = grid[:x, y]
    bottom = grid[x + 1 : len(grid), y]

    return (
        max(left) < value
        or max(right) < value
        or max(top) < value
        or max(bottom) < value
    )


def check_visibility(x, y, grid, value):
    left = list(grid[x, :y])
    right = list(grid[x, y + 1 : len(grid)])
    top = list(grid[:x, y])
    bottom = list(grid[x + 1 : len(grid), y])

    sumLeft = 0

    while len(left) > 0:
        if left.pop(-1) < value:
            sumLeft += 1
        else:
            sumLeft += 1
            break

    sumRight = 0

    while len(right) > 0:
        if right.pop(0) < value:
            sumRight += 1
        else:
            sumRight += 1
            break

    sumTop = 0

    while len(top) > 0:
        if top.pop(-1) < value:
            sumTop += 1
        else:
            sumTop += 1
            break

    sumBot = 0

    while len(bottom) > 0:
        if bottom.pop(0) < value:
            sumBot += 1
        else:
            sumBot += 1
            break

    # print("left: ", sumLeft, "right: ", sumRight, "top: ", sumTop, "bottom: ", sumBot)
    return sumLeft * sumRight * sumTop * sumBot


## Main Code

input = get_input("input.txt")

grid = np.zeros((len(input), len(input)))
for x, line in enumerate(input):
    for y, num in enumerate(line):  # .split():
        grid[x][y] = num

visible = (len(input)) ** 2 - ((len(input) - 2) * (len(input) - 2))

maxVis = 0
maxX, maxY = -1, -1
for x in range(1, len(grid) - 1):
    for y in range(1, len(grid) - 1):
        visible += check_visible(x, y, grid, grid[x, y])
        visibility = check_visibility(x, y, grid, grid[x, y])
        if visibility > maxVis:
            maxVis = visibility
            maxX, maxY = x, y


print(visible)
print(maxVis)
