import os
import sys
from collections import defaultdict
import re


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

word = "XMAS"


def checkXMAS(i, j, results):
    count = 0
    # horizontal up
    if j >= 3:
        if (
            results[i][j - 1] == "M"
            and results[i][j - 2] == "A"
            and results[i][j - 3] == "S"
        ):
            count += 1

    # horizontal down
    if j < len(results[i]) - 3:
        if (
            results[i][j + 1] == "M"
            and results[i][j + 2] == "A"
            and results[i][j + 3] == "S"
        ):
            count += 1

    # vertical up
    if i >= 3:
        if (
            results[i - 1][j] == "M"
            and results[i - 2][j] == "A"
            and results[i - 3][j] == "S"
        ):
            count += 1

    # vertical down
    if i < len(results) - 3:
        if (
            results[i + 1][j] == "M"
            and results[i + 2][j] == "A"
            and results[i + 3][j] == "S"
        ):
            count += 1

    # diagonal left up
    if i >= 3 and j >= 3:
        if (
            results[i - 1][j - 1] == "M"
            and results[i - 2][j - 2] == "A"
            and results[i - 3][j - 3] == "S"
        ):
            count += 1

    # diagnonal right up
    if i >= 3 and j < len(results[i]) - 3:
        if (
            results[i - 1][j + 1] == "M"
            and results[i - 2][j + 2] == "A"
            and results[i - 3][j + 3] == "S"
        ):
            count += 1

    # diagonal left down
    if i < len(results) - 3 and j >= 3:
        if (
            results[i + 1][j - 1] == "M"
            and results[i + 2][j - 2] == "A"
            and results[i + 3][j - 3] == "S"
        ):
            count += 1

    # diagnonal right down
    if i < len(results) - 3 and j < len(results[i]) - 3:
        if (
            results[i + 1][j + 1] == "M"
            and results[i + 2][j + 2] == "A"
            and results[i + 3][j + 3] == "S"
        ):
            count += 1

    return count


def checkX_MAS(i, j, results):
    if (i >= 1 and i < len(results) - 1) and (j >= 1 and j < len(results[0]) - 1):
        if (
            (
                results[i - 1][j - 1] == "M"
                and results[i - 1][j + 1] == "S"
                and results[i + 1][j - 1] == "M"
                and results[i + 1][j + 1] == "S"
            )
            or (
                results[i - 1][j - 1] == "S"
                and results[i - 1][j + 1] == "M"
                and results[i + 1][j - 1] == "S"
                and results[i + 1][j + 1] == "M"
            )
            or (
                results[i - 1][j - 1] == "M"
                and results[i - 1][j + 1] == "M"
                and results[i + 1][j - 1] == "S"
                and results[i + 1][j + 1] == "S"
            )
            or (
                results[i - 1][j - 1] == "S"
                and results[i - 1][j + 1] == "S"
                and results[i + 1][j - 1] == "M"
                and results[i + 1][j + 1] == "M"
            )
        ):
            return 1

    return 0


sum = 0
sumX_MAS = 0
for i, line in enumerate(results):
    for j, letter in enumerate(line):
        if results[i][j] == "X":
            counts = 0
            counts = checkXMAS(i, j, results)
            sum += counts
        if results[i][j] == "A":
            counts = 0
            counts = checkX_MAS(i, j, results)
            sumX_MAS += counts

print(sum)
print(sumX_MAS)
