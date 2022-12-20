import os
import sys
from time import sleep as wait


def get_input(filename: str) -> list[int]:
    """ Using input file, store all integers from separate lines into one array of ints

    Args:
        filename (str): File name of input file

    Returns:
        list[int]: array of numbers from input file
    """
    with open(os.path.join(sys.path[0], filename), 'r') as f:
        input = f.read().splitlines()
        input = [int(x) for x in input]
    return input

# keep track of the indices of each number in an array
# make a numpy array to change all the numbers within a splice based on the movement of the number
# add that array to the indices array

# Modulo the number by the length of the array before movement


def move_number(num: int, original_index: int, indices: list[int], result: list[int]):
    """Move the given number in the original array the amount of times given by its value.

    Args:
        num (int): Number that is to be moved
        original_index (int): Original index of the number in the initial array
        indices (list[int]): Array of the current indices of each number based on index in initial array
        result (list[int]): Resulting array after movement
    """
    # move number based on num (include wrapping)
    current_index = indices[original_index]
    new_index = num + current_index

    if new_index < 0:  # goes too far backwards
        new_index = len(result) - 1 + (new_index % (len(result) - 1))

    if new_index > len(result) - 1:  # goes too far forwards
        new_index = (num + current_index) % (len(result) - 1)

    # modify indices array for all numbers that were affected by movement (ensure no duplicate additions or
    # subtractions by ensuring index to change is different every time)
    if current_index < new_index:
        index_to_change = -1
        for index in range(current_index + 1, new_index + 1):
            previous = index_to_change

            index_to_change = indices.index(index)
            if previous == index_to_change:
                all_indices = [i for i, x in enumerate(indices) if x == index]
                index_to_change = all_indices[1]

            indices[index_to_change] -= 1
    else:
        index_to_change = -1
        for index in range(new_index, current_index):
            previous = index_to_change

            index_to_change = indices.index(index)
            if previous == index_to_change:
                all_indices = [i for i, x in enumerate(indices) if x == index]
                index_to_change = all_indices[1]
            indices[index_to_change] += 1

    # move number into new index and update index accordingly
    result.insert(new_index, result.pop(indices[original_index]))
    indices[original_index] = new_index

    # if there are are ever duplicates in indices
    if len(indices) != len(set(indices)):
        print('LENGTHS NOT EQUAL')
        wait(10)


def get_x_number_after_zero(result: list[int], number: int) -> int:
    """Get the number that is the given number places after zero

    Args:
        result (list[int]): given array of numbers
        number (int): how many places after zero that you need to check

    Returns:
        int: number that is the given number places after zero
    """
    index = result.index(0)
    return result[(index + number) % len(result)]


def main(filename: str):
    input = get_input(filename)

    decrypt_key = 811589153
    input = [x * decrypt_key for x in input]

    # original array and will be looping through to maintain original order of numbers
    original = [*input]

    # indices of each of the original numbers in the initial array, will be modified as indices change
    indices = [i for i, _ in enumerate(input)]

    # array that will be modified and contain final result
    result = [*input]

    # move the number in the result, change the indices in indices
    total_times = 10  # how many runs will occur
    for run in range(total_times):
        print('Run', run + 1)
        percentage = 0
        for original_index, num in enumerate(original):

            # Status of the run
            if (original_index * 100 // len(original) == percentage):
                print(original_index * 100 // len(original), '%')
                percentage += 1

            move_number(num, original_index, indices, result)

    print(result)
    print(get_x_number_after_zero(result, 1000))
    print(get_x_number_after_zero(result, 2000))
    print(get_x_number_after_zero(result, 3000))
    print(sum([get_x_number_after_zero(result, 1000), get_x_number_after_zero(result, 2000),
               get_x_number_after_zero(result, 3000)]))


main('input.txt')

# 0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459
