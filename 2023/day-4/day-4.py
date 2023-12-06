import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

# 10 winning numbers in test
points = 0

winningNumbers = 10
match = 0
firstMatchPoints = 0
points = 0

dict = {}

for i in range(1, len(results) + 1):
    dict[i] = 1
print(dict)

print(len(results))

for i in range(0, len(results)):
    match = 0
    firstMatchPoints = 0

    nums = [int(num) for num in results[i].split(" ") if num.isdigit()]
    print(nums)
    winNums = nums[:winningNumbers]
    ourNums = nums[winningNumbers:]
    print("win", winNums)
    print("our", ourNums)

    for num in ourNums:
        if num in winNums:
            # if match == 0:
            #     match = 1
            #     firstMatchPoints = 1
            # else:
            #     firstMatchPoints *= 2
            match += 1

    for j in range(1, match + 1):
        print(j)
        print(j + i + 1)
        if not (j + i + 1) > len(results):
            dict[j + i + 1] = dict.get(j + i + 1, 1) + (1 * dict.get(i + 1, 1))
    print(dict)
    # points += firstMatchPoints
    # print(points)

for key, value in dict.items():
    points += value

# points += len(results)

print(points)
