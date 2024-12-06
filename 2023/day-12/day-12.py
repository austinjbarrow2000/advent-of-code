import os
import sys


def generate_combinations(springs, unknowns, index, combinations):
    if index == len(unknowns):
        combinations.append(springs.copy())
        # print(springs)
        return

    # Set current unknown to '#'
    springs[unknowns[index]] = "#"
    generate_combinations(springs, unknowns, index + 1, combinations)

    # Set current unknown to '.'
    springs[unknowns[index]] = "."
    generate_combinations(springs, unknowns, index + 1, combinations)

    # Reset the value for backtracking
    springs[unknowns[index]] = "."


def areEqual(arr1, arr2, N, M):
    # If lengths of array are not
    # equal means array are not equal
    if N != M:
        return False

    # Linearly compare elements
    for i in range(0, N):
        if arr1[i] != arr2[i]:
            return False

    # If all elements were same.
    return True


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

sum = 0
countLine = 0
for line in results:
    line = line.split(" ")
    # print(line)
    nums = [int(num) for num in line[1].split(",") if num.isdigit()]
    numbers = []
    for i in range(0, 5):
        for num in nums:
            numbers.append(num)
    print(numbers)
    springs = list(line[0])
    for i in range(0, 5):
        springs.append("?")
        for char in list(line[0]):
            springs.append(char)

    unknowns = []
    print(springs)

    for i in range(0, len(springs)):
        if springs[i] == "?":
            unknowns.append(i)

    # for unknown in unknowns:
    #     springs[unknown] = "#"

    # test every combination of unknowns as # or .
    # if the combination works, add it to the list of springs
    # if the combination doesn't work, remove it from the list of springs
    # repeat until there are no more unknowns

    # print(springs)
    # for i in range(0, len(unknowns)):
    #     springs[unknowns[i]] = "#"
    #     for j in range(i + 1, len(unknowns)):
    #         springs[unknowns[j]] = "."
    #         print(springs)

    # for i in range(0, len(unknowns)):
    #     springs[unknowns[i]] = "."
    #     for j in range(i + 1, len(unknowns)):
    #         springs[unknowns[j]] = "#"
    #         print(springs)

    combinations = []
    generate_combinations(springs, unknowns, 0, combinations)

    arrangements = 0
    for combination in combinations:
        countArray = []
        count = 0
        for i in range(0, len(combination)):
            if combination[i] == "#":
                count += 1
            if (combination[i] == "." and count != 0) or (
                i == len(combination) - 1 and count != 0
            ):
                countArray.append(count)
                count = 0

        # print(combination)
        # print(countArray)
        # print(numbers)
        if areEqual(countArray, numbers, len(countArray), len(numbers)):
            arrangements += 1
            # print("arrangement works")
    # print("arrangements:", arrangements)
    sum += arrangements

    # if countLine == 3:
    #     break
    countLine += 1
    print(countLine)
print(sum)
