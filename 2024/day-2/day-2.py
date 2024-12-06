import os
import sys
from collections import defaultdict


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

print(results)
sum = 0
for line in results:
    newArray = []
    line = line.split()
    for i, num in enumerate(line):
        if i != len(line) - 1:
            newArray.append(int(line[i]) - int(line[i + 1]))
    safe = 0

    if not (
        (any(x < 0 for x in newArray) and any(x > 0 for x in newArray))
        or 0 in newArray
        or any(abs(x) > 3 for x in newArray)
    ):
        safe = 1
    else:
        for i, num in enumerate(line):
            newArray = []
            test = line.copy()
            test.pop(i)
            print(test, line)
            for i, num in enumerate(test):
                if i != len(test) - 1:
                    newArray.append(int(test[i]) - int(test[i + 1]))

            if not (
                (any(x < 0 for x in newArray) and any(x > 0 for x in newArray))
                or 0 in newArray
                or any(abs(x) > 3 for x in newArray)
            ):
                safe = 1
    if safe == 1:
        sum += 1

print(sum)
# 665
