import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

colors = ["red", "green", "blue"]

numGames = 0
sum = 0
for game in results:
    game = game.replace(":", "")
    game = game.replace(";", "")
    game = game.replace(",", "")
    print(game)
    maxColor = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    nums = [num for num in game.split(" ") if num.isdigit() or num in colors]
    print(nums)
    for i in range(0, len(nums)):
        if nums[i] in colors:
            maxColor[nums[i]] = max(int(nums[i - 1]), maxColor[nums[i]])

    # if maxColor["red"] <= 12 and maxColor["green"] <= 13 and maxColor["blue"] <= 14:
    #     print(int(nums[0]))
    #     print(maxColor)
    #     numGames += int(nums[0])

    sum += maxColor["red"] * maxColor["green"] * maxColor["blue"]

print(sum)
