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
array1, array2 = [], []
for line in results:
    line = line.split()
    array1.append(line[0])
    array2.append(line[1])

array1.sort()
array2.sort()

newArray = (abs(int(num1) - int(num2)) for num1, num2 in zip(array1, array2))
print(sum(newArray))

counts = defaultdict(lambda: 0)

for num in array2:
    counts[int(num)] += 1

result = 0
for num in array1:
    print(int(num))
    print(counts[int(num)])
    result += int(num) * counts[int(num)]

print(result)
