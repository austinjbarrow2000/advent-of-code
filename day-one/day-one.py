from mergesort import *


def get_input(filename):
    input_file = open(filename, "r")
    results = input_file.read().splitlines()
    input_file.close()
    return results


filename = "day-one/input-calories.txt"
results = get_input(filename)

totalCalories = []
sum = 0
for num in results:
    if num == "":
        totalCalories.append(sum)
        sum = 0
    else:
        sum += int(num)

sortedCalories = mergesort(totalCalories)
print(sortedCalories)

topThree = 0
for i in range(0, 3):
    topThree += sortedCalories[i]
print(topThree)
