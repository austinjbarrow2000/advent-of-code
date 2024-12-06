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

rules = defaultdict(list)
update_mode = 0
updates = []
for line in results:
    if line == "":
        update_mode = 1
    elif update_mode == 0:
        rule = line.split("|")
        rules[rule[0]].append(rule[1])
    elif update_mode == 1:
        updates.append(line.split(","))

result = 0
incorrect = []
for update in updates:
    success = 1
    for i, number in enumerate(update):
        temp = update[0:i]
        if any((num in rules[number]) for num in temp):
            success = 0
            incorrect.append(update)
            break

    if success:
        result += int(update[math.floor(len(update) / 2)])

print(result)

for key, rule in rules.items():
    print(key, rule)
notDone = 1
result = 0
print(len(incorrect))
count = 0
for update in incorrect:
    print("Update ", count)
    while notDone:
        insert = 0
        for i, number in enumerate(update):
            # if any((num in rules[number]) for num in temp):
            # print(number)
            temp = update[0:i]
            index = next(
                (j for j, num in enumerate(temp) if num in rules[number]), None
            )
            # print(index)
            if index != None:
                insert = 1
                # print(update)
                popped_num = update.pop(index)
                # print(update)
                update.insert(i, popped_num)
                # print(update)
                break
        if insert == 0:
            notDone = 0
            count += 1

    notDone = 1
    result += int(update[math.floor(len(update) / 2)])

    print(update)
print(result)
