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


def calcResults(nums, results):
    if len(nums) == 0:
        return results
    arr = []
    num = int(nums.pop(0))
    for res in results:
        arr.append(res + num)
        arr.append(res * num)
        arr.append(int(str(res) + str(num)))

    return calcResults(nums, arr)

    return arr.copy()


res = 0
for i, line in enumerate(results):
    print(i)
    arr = line.split(" ")
    arr[0] = arr[0][0:-1]
    # print(arr)
    final = arr.pop(0)
    results = [0]
    results = calcResults(arr, results)
    # print(results)
    if int(final) in results:
        res += int(final)

print(res)
