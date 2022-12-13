# get input
import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        input = f.read().split("\n\n")
        input = [line.split("\n") for line in input]
    return input


def get_input_pt2(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        input = f.read().split("\n")
        input = [i for i in input if i != ""]
    return input


# compare pairs function
def compare_pair(pair):
    pair1 = eval(pair[0])
    pair2 = eval(pair[1])

    # print(pair1, pair2)

    while len(pair1) > 0 and len(pair2) > 0:
        left = pair1.pop(0)
        right = pair2.pop(0)
        # print(left, right)

        if isinstance(left, int) and isinstance(right, int):
            if left > right:
                return False
            elif left < right:
                return True
            else:
                continue
        elif isinstance(left, list) and not isinstance(right, list):
            right = [right]

        elif not isinstance(left, list) and isinstance(right, list):
            left = [left]

        result = compare_pair([str(left), str(right)])
        if result == "Continue":
            continue
        if result:
            return True  # THIS IS WHERE THE ISSUE IS
        else:
            return False

    if len(pair1) > 0 and len(pair2) == 0:
        return False

    if len(pair1) == 0 and len(pair2) > 0:
        return True
    return "Continue"  # This means they got to end, were equal length, and no condition reached


# main function
def main(filename):
    input = get_input(filename)
    sumCorrectOrder = 0
    for i, pair in enumerate(input, start=1):
        result = compare_pair(pair)
        if result == "Continue" or result:
            print(result)
            print(i)
            sumCorrectOrder += i
    print(sumCorrectOrder)


main("input.txt")


def merge(arr_one, arr_two):
    result = []
    while len(arr_one) > 0 and len(arr_two) > 0:
        comparison = compare_pair([arr_one[0], arr_two[0]])
        if comparison == "Continue" or comparison:
            result.append(arr_one.pop(0))
        else:
            result.append(arr_two.pop(0))
    while len(arr_one) > 0:
        result.append(arr_one.pop(0))
    while len(arr_two) > 0:
        result.append(arr_two.pop(0))

    return result


def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    arr_one = mergesort(arr[:mid])
    arr_two = mergesort(arr[mid:])
    return merge(arr_one, arr_two)


def part2(filename):
    input = get_input_pt2(filename)
    result = mergesort(input)
    key = 1
    for i, val in enumerate(result, start=1):
        print(val)
        if val == "[[2]]" or val == "[[6]]":
            print("hi")
            key *= i
    print("key", key)


part2("part2input.txt")
# 5588 is correct!
# 5735 too high

# return True  # THIS IS WHERE THE ISSUE IS

# 5233 too low ()

# if len(left) == len(right):
#     continue
# return True  # THIS IS WHERE THE ISSUE IS
