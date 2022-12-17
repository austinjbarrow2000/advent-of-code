import os
import sys


# get input
def get_input(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as f:
        input = f.read().splitlines(0)
    return input[0]


# define way to create shapes from bottom left edge in numbers (bottom = 3 above top rock/floor, left = 2 from wall)
# start = (2,bottom)
def create_shape(start, shape):
    # dx, dy
    flatLine = [(0, 0), (1, 0), (2, 0), (3, 0)]
    plus = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
    backL = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    tallLine = [(0, 0), (0, 1), (0, 2), (0, 3)]
    square = [(0, 0), (1, 0), (0, 1), (1, 1)]

    shape_coords = []
    return shape_coords


# move shape according to movements key until any part of rock hits bottom or another rock
# dont execute move if would hit wall
# return new bottom position
def move_shape(grid, shape_coords, movements):
    newBottom = 0
    return newBottom

# main function


def main(filename):
    shapes = ['flatLine', 'plus', 'backL', 'tallLine', 'square']
    # dx, dy
    flatLine = [(0, 0), (1, 0), (2, 0), (3, 0)]
    plus = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
    backL = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    tallLine = [(0, 0), (0, 1), (0, 2), (0, 3)]
    square = [(0, 0), (1, 0), (0, 1), (1, 1)]

    chamber = {}

    # get input
    movements = get_input(filename)

    # run for loop (over number of rocks)
    numRocks = 2022
    bottom = 0
    for i in range(numRocks):
        create_shape((bottom, 2), shapes[i % (len(shapes))])


main("input.txt")
