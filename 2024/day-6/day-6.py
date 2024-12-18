import os
import sys
from collections import defaultdict
import re
import math


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

for i, line in enumerate(results):
    for j, char in enumerate(line):
        if char == "^":
            guard_i, guard_j = i, j
            yay_i, yay_j = i, j


visited = defaultdict(list)

# directions up, right, down, left

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0
# 0 up, 1 right, 2 down, 3 left
print(guard_i, guard_j)

blockages = {}
wall = defaultdict(lambda: 0)

# while (
#     guard_i < len(results)
#     and guard_j < len(results[0])
#     and guard_i >= 0
#     and guard_j >= 0
# ):
#     # print(guard_i, guard_j)
#     temp_i, temp_j = guard_i, guard_j
#     while 1:
#         if ((direction + 1) % 4) in visited[(guard_i, guard_j)]:
#             blockages[
#                 (
#                     guard_i + directions[direction][0],
#                     guard_j + directions[direction][1],
#                 )
#             ] = 1
#             break

#         temp_i, temp_j = (
#             temp_i + directions[(direction + 1) % 4][0],
#             temp_j + directions[(direction + 1) % 4][1],
#         )
#         if (
#             temp_i < len(results)
#             and temp_j < len(results[0])
#             and temp_i >= 0
#             and temp_j >= 0
#             and guard_i + directions[direction][0] < len(results)
#             and guard_j + directions[direction][1] < len(results[0])
#             and guard_i + directions[direction][0] >= 0
#             and guard_j + directions[direction][1] >= 0
#         ):
#             if (temp_i, temp_j) in visited and ((direction + 1) % 4) in visited[
#                 (temp_i, temp_j)
#             ]:
#                 blockages[
#                     (
#                         guard_i + directions[direction][0],
#                         guard_j + directions[direction][1],
#                     )
#                 ] = 1
#                 break
#         else:
#             break
#     # if (
#     #     (guard_i, guard_j) in visited
#     #     and ((direction + 1) % 4) in visited[(guard_i, guard_j)]
#     #     and guard_i + directions[direction][0] < len(results)
#     #     and guard_j + directions[direction][1] < len(results[0])
#     #     and guard_i + directions[direction][0] >= 0
#     #     and guard_j + directions[direction][1] >= 0
#     # ):
#     #     blockages[
#     #         (guard_i + directions[direction][0], guard_j + directions[direction][1])
#     #     ] = 1

#     visited[(guard_i, guard_j)].append(direction)
#     if (
#         guard_i + directions[direction][0] < len(results)
#         and guard_j + directions[direction][1] < len(results[0])
#         and guard_i + directions[direction][0] >= 0
#         and guard_j + directions[direction][1] >= 0
#     ):
#         if (
#             results[guard_i + directions[direction][0]][
#                 guard_j + directions[direction][1]
#             ]
#             == "#"
#         ):
#             wall[
#                 (guard_i + directions[direction][0], guard_j + directions[direction][1])
#             ] = 1
#             direction = (direction + 1) % 4
#         else:
#             guard_i += directions[direction][0]
#             guard_j += directions[direction][1]
#     else:
#         break

guard_i, guard_j = yay_i, yay_j
blockages = {}
print(guard_i, guard_j)

while (
    guard_i < len(results)
    and guard_j < len(results[0])
    and guard_i >= 0
    and guard_j >= 0
):
    # print(guard_i, guard_j)
    temp_i, temp_j = guard_i, guard_j
    while 1:
        if (
            ((direction + 1) % 4) in visited[(guard_i, guard_j)]
            and guard_i + directions[direction][0] < len(results)
            and guard_j + directions[direction][1] < len(results[0])
            and guard_i + directions[direction][0] >= 0
            and guard_j + directions[direction][1] >= 0
            and results[guard_i + directions[direction][0]][
                guard_j + directions[direction][1]
            ]
            != "#"
        ):
            blockages[
                (
                    guard_i + directions[direction][0],
                    guard_j + directions[direction][1],
                )
            ] = 1
            break
        if (
            temp_i + directions[(direction + 1) % 4][0] < len(results)
            and temp_j + directions[(direction + 1) % 4][1] < len(results[0])
            and temp_i + directions[(direction + 1) % 4][0] >= 0
            and temp_j + directions[(direction + 1) % 4][1] >= 0
            and results[temp_i + directions[(direction + 1) % 4][0]][
                temp_j + directions[(direction + 1) % 4][1]
            ]
            == "#"
        ):
            if (temp_i, temp_j) in visited and ((direction + 2) % 4) in visited[
                (temp_i, temp_j)
            ]:
                blockages[
                    (
                        guard_i + directions[direction][0],
                        guard_j + directions[direction][1],
                    )
                ] = 1
                break
            break

        temp_i, temp_j = (
            temp_i + directions[(direction + 1) % 4][0],
            temp_j + directions[(direction + 1) % 4][1],
        )

        if (
            temp_i < len(results)
            and temp_j < len(results[0])
            and temp_i >= 0
            and temp_j >= 0
            and guard_i + directions[direction][0] < len(results)
            and guard_j + directions[direction][1] < len(results[0])
            and guard_i + directions[direction][0] >= 0
            and guard_j + directions[direction][1] >= 0
            and results[guard_i + directions[direction][0]][
                guard_j + directions[direction][1]
            ]
            != "#"
        ):
            if results[temp_i][temp_j] == "#":
                break

            if (temp_i, temp_j) in visited and ((direction + 1) % 4) in visited[
                (temp_i, temp_j)
            ]:
                blockages[
                    (
                        guard_i + directions[direction][0],
                        guard_j + directions[direction][1],
                    )
                ] = 1
                break
        else:
            break
    # if (
    #     (guard_i, guard_j) in visited
    #     and ((direction + 1) % 4) in visited[(guard_i, guard_j)]
    #     and guard_i + directions[direction][0] < len(results)
    #     and guard_j + directions[direction][1] < len(results[0])
    #     and guard_i + directions[direction][0] >= 0
    #     and guard_j + directions[direction][1] >= 0
    # ):
    #     blockages[
    #         (guard_i + directions[direction][0], guard_j + directions[direction][1])
    #     ] = 1

    visited[(guard_i, guard_j)].append(direction)
    if (
        guard_i + directions[direction][0] < len(results)
        and guard_j + directions[direction][1] < len(results[0])
        and guard_i + directions[direction][0] >= 0
        and guard_j + directions[direction][1] >= 0
    ):
        if (
            results[guard_i + directions[direction][0]][
                guard_j + directions[direction][1]
            ]
            == "#"
        ):
            direction = (direction + 1) % 4
        else:
            guard_i += directions[direction][0]
            guard_j += directions[direction][1]
    else:
        break

print(len(visited))
print(len(blockages))
if (yay_i, yay_j) in blockages:
    print("Yay")
# print(blockages.keys())


# def save_visualization(results, visited, blockages, output_filename):
#     # Convert results into a mutable list of lists
#     grid = [list(line) for line in results]

#     # Mark visited cells with 'V'
#     for i, j in visited.keys():
#         if grid[i][j] == ".":
#             grid[i][j] = "."  # grid[i][j] + str(visited[i, j][0])

#     # Mark blockages with 'B'
#     for i, j in blockages.keys():
#         grid[i][j] = grid[i][j] + "O"

#     # Write the grid to a file
#     with open(output_filename, "w") as f:
#         for line in grid:
#             f.write("".join(line) + "\n")


# # After your main processing logic:
# output_filename = "visualization.txt"
# save_visualization(results, visited, blockages, output_filename)
# print(f"Visualization saved to {output_filename}")


def save_visualization(results, visited, blockages, output_filename):
    # Convert results into a mutable list of lists
    grid = [list(line) for line in results]

    # Define direction symbols
    dir_symbols = {0: "↑", 1: "→", 2: "↓", 3: "←"}

    # Mark visited cells with direction arrows
    for (i, j), directions in visited.items():
        if grid[i][j] == ".":
            grid[i][j] = dir_symbols[directions[-1]]  # Use the last direction

    # Mark blockages with 'B'
    for i, j in blockages.keys():
        grid[i][j] = "B"

    grid[yay_i][yay_j] = "Y"

    # Write the grid to a file with proper spacing
    with open(output_filename, "w") as f:
        for line in grid:
            f.write(" ".join(line) + "\n")


# After your main processing logic:
output_filename = "visualization.txt"
save_visualization(results, visited, blockages, output_filename)
print(f"Visualization saved to {output_filename}")
