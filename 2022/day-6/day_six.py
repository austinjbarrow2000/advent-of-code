import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


input = get_input("input.txt")

input = list(input[0])
marker = []

processed = 0
while len(set(marker)) != 4:
    if len(marker) == 4:
        marker.pop(0)
    marker.append(input.pop(0))
    processed += 1
print(processed)

input = get_input("input.txt")
input = list(input[0])
marker = []

processed = 0
while len(set(marker)) != 14:
    if len(marker) == 14:
        marker.pop(0)
    marker.append(input.pop(0))
    processed += 1

print(processed)
