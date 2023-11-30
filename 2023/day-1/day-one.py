import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

# totalCalories = []
# sum = 0
# for num in results:
#     if num == "":
#         totalCalories.append(sum)
#         sum = 0
#     else:
#         sum += int(num)

# sortedCalories = mergesort(totalCalories)
# print(sortedCalories)

# topThree = 0
# for i in range(0, 3):
#     topThree += sortedCalories[i]
# print(topThree)
