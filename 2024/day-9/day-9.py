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

disk_map = results[0]
print(len(disk_map))
