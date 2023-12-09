import os
import sys
import re


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

# sum = 0
part2sum = 0
for line in results:
    sequence = [int(num) for num in line.split(" ")]
    nextarrays = []
    nextarrays.append(sequence)
    while nextarrays[-1].count(0) != len(nextarrays[-1]):
        temparray = []
        for i in range(1, len(nextarrays[-1])):
            temparray.append(nextarrays[-1][i] - nextarrays[-1][i - 1])
        nextarrays.append(temparray)

    # print(nextarrays)
    # for j in range(len(nextarrays) - 1, -1, -1):
    #     sum += nextarrays[j][-1]
    #     # print(sum)
    difference = 0
    for j in range(len(nextarrays) - 2, -1, -1):
        difference = nextarrays[j][0] - difference
    part2sum += difference

    #     sum += nextarrays[j][-1]
    #     # print(sum)

print(part2sum)
# print(sum)
