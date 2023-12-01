import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)


numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def extract_numbers_and_words(s):
    result = ""
    current_word = ""
    for char in s:
        # print("char:" + char)
        # print("current:" + current_word)
        # print("result:" + result)
        if char.isalpha():
            current_word += char
        elif char.isdigit():
            result += char
            current_word = ""
        else:
            current_word = ""

        for key in numbers.keys():
            if key in current_word:
                result += numbers.get(key)
                current_word = current_word[-1:]

    return result


sum = 0
for str1 in results:
    result = extract_numbers_and_words(str1)
    print("result: " + result)
    result_int = result[0] + result[-1]
    print(result_int)

    sum += int(result_int)

print(sum)
