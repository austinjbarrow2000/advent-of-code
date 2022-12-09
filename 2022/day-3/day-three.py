import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


# def findCommon(rucksack1, rucksack2):
#     common = ord(list(rucksack1.intersection(rucksack2)).pop())
#     if common > 96 and common < 123:
#         return common - 96
#     return common - 38


def findCommon(rucksackGroup):
    print(list(set.intersection(*rucksackGroup)))
    common = ord(list(set.intersection(*rucksackGroup)).pop())
    if common > 96 and common < 123:
        return common - 96
    return common - 38


rucksacks = get_input("input.txt")
result = 0
groupRucksack = []
resultTwo = 0

for rucksack in rucksacks:
    mid = len(rucksack) // 2
    result += findCommon([set(rucksack[:mid]), set(rucksack[mid:])])

    if len(groupRucksack) < 2:
        groupRucksack.append(set(rucksack))
    else:
        groupRucksack.append(set(rucksack))
        resultTwo += findCommon(groupRucksack)
        groupRucksack = []


print(result)
print(resultTwo)
