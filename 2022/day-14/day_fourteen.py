# get input
import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        input = f.read().splitlines()
        input = [line.split(" -> ") for line in input]
    return input


# parse input (tiles of # get put into an array)
def get_rocks(input):
    bottomRow = 0
    rocks = {}
    for line in input:
        for num in range(0, len(line) - 1):
            col1, row1 = line[num].split(",")
            col2, row2 = line[num + 1].split(",")
            col1, row1, col2, row2 = int(col1), int(row1), int(col2), int(row2)
            for col in range(min(col1, col2), max(col1, col2) + 1):
                rocks[col, row1] = "#"
            for row in range(min(row1, row2), max(row1, row2) + 1):
                rocks[col1, row] = "#"

            if max(row1, row2) > bottomRow:
                bottomRow = max(row1, row2)

    return rocks, bottomRow


# simulate sand (get start and simulate sand falling and wait until sand goes beyong the lowest #)
def simulate_sand(rocks, bottomRow, part):
    start = (500, 0)
    restingSand = {}
    x, y = start

    # y+1 != bottomRow + 2 only really checked for part2:
    while (part == 1 and y < bottomRow) or (start not in restingSand and part == 2):
        if (x, y + 1) not in rocks and (x, y + 1) not in restingSand and y+1 != bottomRow + 2:  # Step below not blocked
            x, y = x, y + 1
        else:
            # Step below and left not blocked
            if (x - 1, y + 1) not in rocks and (x - 1, y + 1,) not in restingSand and y+1 != bottomRow + 2:
                x, y = x - 1, y + 1
            # Step below and right not blocked
            elif (x + 1, y + 1) not in rocks and (x + 1, y + 1) not in restingSand and y+1 != bottomRow + 2:
                x, y = x + 1, y + 1
            else:
                restingSand[x, y] = 'o'
                x, y = start

    return restingSand


# main function
def main(filename):
    input = get_input(filename)
    rocks, bottomRow = get_rocks(input)
    print(len(simulate_sand(rocks, bottomRow, 1).keys()))
    print(len(simulate_sand(rocks, bottomRow, 2).keys()))


main("input.txt")
