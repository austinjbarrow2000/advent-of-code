import os
import sys
from time import sleep as wait
import numpy as np


# get input
def get_input(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as f:
        input = f.read()
    return list(input)


# define way to create shapes from top left edge in numbers (top = 3 above top rock/floor, left = 2 from wall)
# start = (2,top)
def create_shape(chamber, start, shape):
    # dx, dy Coordinates to put the bottom left of the shape
    dx, dy = start

    shape_coords = [(dx + x, dy + y) for x, y in shape]
    for coord in shape_coords:
        chamber[coord] = '#'
    return shape_coords


# move shape according to movements key until any part of rock hits top or another rock
# dont execute move if would hit wall
# return new top position
def move_shape(top, chamber, shape_coords, movements, moveIndex):
    top = top
    finishMove = False
    while not finishMove:
        # wait(0.5)

        # get current move
        move = movements[moveIndex % len(movements)]

        # print(move)
        # remove all old coordinates from chamber
        for coord in shape_coords:
            chamber.pop(coord)

        oldCoords = shape_coords
        newCoords = []
        if move == '>':
            # shift coords to right, if hit wall convert back and do nothing
            for coord in shape_coords:
                coord = (coord[0] + 1, coord[1] + 0)
                newCoords.append(coord)
                if coord[0] < 0 or coord[0] > 6 or coord in chamber:
                    newCoords = oldCoords
                    break
            oldCoords = newCoords
            shape_coords = newCoords
            #print('right', shape_coords)

        elif move == '<':
            # shift coords to left, if hit wall convert back and do nothing
            for coord in shape_coords:
                coord = (coord[0] - 1, coord[1] + 0)
                newCoords.append(coord)
                if coord[0] < 0 or coord[0] > 6 or coord in chamber:
                    newCoords = oldCoords
                    break
            oldCoords = newCoords
            shape_coords = newCoords
            #print('left', shape_coords)

        newCoords = []
        for coord in shape_coords:
            coord = (coord[0] + 0, coord[1] - 1)
            # Check if coord hits other rock or floor, convert back if does and set finishMove
            newCoords.append(coord)
            if coord in chamber or coord[1] == 0:
                newCoords = oldCoords
                finishMove = True
                #print('Final Shape', newCoords)

                break
        shape_coords = newCoords
        #print('new', shape_coords)

        # set all coords in chamber to rock and new top
        maxY = 0
        for coord in shape_coords:
            chamber[coord] = '#'
            if (coord[1] > maxY and finishMove):
                #print("COORD 1", coord[1])
                maxY = coord[1]

        # update top if finishMove = true
        if maxY > top and finishMove:
            top = maxY

        moveIndex += 1
    return top, moveIndex


# main function
def main(filename):
    # dx, dy
    flatLine = [(0, 0), (1, 0), (2, 0), (3, 0)]
    plus = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
    backL = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    tallLine = [(0, 0), (0, 1), (0, 2), (0, 3)]
    square = [(0, 0), (1, 0), (0, 1), (1, 1)]

    shapes = [flatLine, plus, backL, tallLine, square]

    chamber = {}

    # get input
    movements = get_input(filename)

    # run for loop (over number of rocks)
    numRocks = 1000000000000
    top = 0
    moveIndex = 0
    i = 0
    num = 1000
    extra = 0
    countRocks = []
    while i < numRocks:
        # wait(0.01)
        # for i in range(numRocks):
        print(i)
        print((i / numRocks) * 100, '%')
        # print(numRocks, i)
        #print(numRocks - i, 'yo')
        # print(top)
        # if top == 13066 + 2:
        #     countRocks.append(i)
        # if top == (13066 + 2548 + 2):
        #     countRocks.append(i)

        # print('rocks', countRocks)
        # 680

        if i >= (20000) and (numRocks - i > (1690 * num)):
            print('rocks', countRocks)
            print('i', i)
            extra += 2548 * num  # 81 * num  # how many rows is it not how many rocks
            i += 1690 * num  # how many rocks are added
            continue

        # For test, rows increased by 53 for every 35 rocks
        # 1514285714288

        # For input, rows increased by for every rocks

        # 2360, 442

        # Repeats (680, 147)

        # Can see it repeats
        # if i == 13000:
        #     # np.zeros((2000, 8), int)
        #     array = np.empty(shape=(3000, 8), dtype=str)
        #     keys = [key for key in chamber.keys() if key[1] >
        #             10000 and key[1] < 13000]
        #     for key in keys:
        #         print(key[0], key[1])
        #         array[key[1] - 10000][key[0]] = '■'
        #     # print(empty_array)
        #     array = np.flip(array)
        #     copy = array[1000]
        #     for idx, row in enumerate(array):
        #         print(3009 - idx, end=" ")
        #         for value in row:
        #             if (value == ''):
        #                 print(' ', end="")
        #             print(value, end="")
        #         #print([*row], [*copy], end="")
        #         if [*row] == [*copy]:
        #             print('beep', end="")
        #         print(" ")

        #     wait(10)

        # 1702
        # 1269,
        # 551, 373
        # 793

        # 46, 99, 152, 205, 258 repeats

        # Check for repeating 10 columns
        # if top
        # print(top)
        # if top == 301:
        #     firstRepeat = [(key[0], key[1]-300+4) for key in chamber.keys() if (
        #         key[1] < 300 and key[1] >= 300 - 3)]
        #     nextMove = moveIndex
        #     nextShape = shapes[i % (len(shapes))]
        #     print(firstRepeat)
        #     wait(5)
        # if top > 301:
        #     top30 = [(key[0], key[1]-top+4) for key in chamber.keys() if (
        #         key[1] < top and key[1] >= top - 3)]
        #     print(top)
        #     print(top30)
        #     print(firstRepeat)
        #     wait(1)
        #     num = 0
        #     for key in firstRepeat:
        #         if key[1] in top30:
        #             num += 1
        #     if num == len(firstRepeat):
        #         # if bottom30 == top30:
        #         print('YAY')
        #         wait(10)

        # Check for repeats
        # if i > 31:
        #     same = True
        #     top30 = [(key[0], key[1]-top+31) for key in chamber.keys() if (
        #         key[1] < top and key[1] >= top - 30)]
        #     bottom30 = [key for key in chamber.keys() if key[1] < 31]
        #     #print('top', top30)
        #     #print('bot', bottom30)
        #     wait(2)
        #     for key in top30:
        #         if key not in bottom30:
        #             same = False
        #     if same:
        #         print(top30)
        #         print(bottom30)
        #         wait(5)

        shape = create_shape(chamber, (2, top + 4),
                             shapes[i % (len(shapes))])
        top, moveIndex = move_shape(
            top, chamber, shape, movements, moveIndex)

        i += 1

    print(top)
    print(extra)
    print(top + extra)


main("input.txt")
