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

sum = 0
disabled = 0
for line in results:
    multiply = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)
    for pair in multiply:
        print(pair)
        if "do()" in pair:
            disabled = 0
        elif "don't()" in pair:
            disabled = 1
        elif disabled == 0:
            sum += int(pair[0]) * int(pair[1])

print(sum)
