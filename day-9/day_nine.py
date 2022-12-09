import numpy as np

# get input
def get_input(filename):
    file = open(filename, "r")
    input = file.read().splitlines()
    return input


# is Head Adjacent to Tail Check (Also no movement if H is overlapping)
def adjacency_check(head, tail):
    tailPositionX = tail.positionX
    tailPositionY = tail.positionY
    adjacent = []

    adjacent.append([tailPositionX - 1, tailPositionY - 1])
    adjacent.append([tailPositionX, tailPositionY - 1])
    adjacent.append([tailPositionX + 1, tailPositionY - 1])
    adjacent.append([tailPositionX - 1, tailPositionY])
    adjacent.append([tailPositionX, tailPositionY])
    adjacent.append([tailPositionX + 1, tailPositionY])
    adjacent.append([tailPositionX - 1, tailPositionY + 1])
    adjacent.append([tailPositionX, tailPositionY + 1])
    adjacent.append([tailPositionX + 1, tailPositionY + 1])

    return [head.positionX, head.positionY] in adjacent


# Head Movement Function (trickle down movement for tail) WAS USED FOR PART 1 NOW MODIFIED FOR BOTH
# def head_movement(head, tail, line):
#     direction, magnitude = line.split(" ")
#     magnitude = int(magnitude)
#     if direction == "R":
#         for i in range(magnitude):
#             head.update_position(head.positionX + 1, head.positionY)  # Move right
#             tail_movement(head, tail)
#     elif direction == "L":
#         for i in range(magnitude):
#             head.update_position(head.positionX - 1, head.positionY)  # Move left
#             tail_movement(head, tail)
#     elif direction == "U":
#         for i in range(magnitude):
#             head.update_position(head.positionX, head.positionY - 1)  # Move up
#             tail_movement(head, tail)
#     elif direction == "D":
#         for i in range(magnitude):
#             head.update_position(head.positionX, head.positionY + 1)  # Move Down
#             tail_movement(head, tail)


# Head Movement Function (trickle down movement for rest of rope)
def head_movement_long(head, line, rope):
    direction, magnitude = line.split(" ")
    magnitude = int(magnitude)
    if direction == "R":
        for i in range(magnitude):
            head.update_position(head.positionX + 1, head.positionY)  # Move right
            for i in range(len(rope) - 1):
                tail_movement(rope[i], rope[i + 1])
    elif direction == "L":
        for i in range(magnitude):
            head.update_position(head.positionX - 1, head.positionY)  # Move left
            for i in range(len(rope) - 1):
                tail_movement(rope[i], rope[i + 1])
    elif direction == "U":
        for i in range(magnitude):
            head.update_position(head.positionX, head.positionY - 1)  # Move up
            for i in range(len(rope) - 1):
                tail_movement(rope[i], rope[i + 1])
    elif direction == "D":
        for i in range(magnitude):
            head.update_position(head.positionX, head.positionY + 1)  # Move Down
            for i in range(len(rope) - 1):
                tail_movement(rope[i], rope[i + 1])


# Tail Movement Function
def tail_movement(head, tail):
    if adjacency_check(head, tail):
        return
    else:
        if head.positionX > tail.positionX and head.positionY == tail.positionY:
            tail.update_position(tail.positionX + 1, tail.positionY)
            # Move right

        elif head.positionX < tail.positionX and head.positionY == tail.positionY:
            tail.update_position(tail.positionX - 1, tail.positionY)
            # Move left

        elif head.positionX == tail.positionX and head.positionY < tail.positionY:
            tail.update_position(tail.positionX, tail.positionY - 1)
            # Move Up

        elif head.positionX == tail.positionX and head.positionY > tail.positionY:
            tail.update_position(tail.positionX, tail.positionY + 1)
            # Move Down

        elif head.positionX < tail.positionX and head.positionY < tail.positionY:
            tail.update_position(tail.positionX - 1, tail.positionY - 1)
            # Diagonal Up Left

        elif head.positionX > tail.positionX and head.positionY < tail.positionY:
            tail.update_position(tail.positionX + 1, tail.positionY - 1)
            # Diagonal Up Right

        elif head.positionX < tail.positionX and head.positionY > tail.positionY:
            tail.update_position(tail.positionX - 1, tail.positionY + 1)
            # Diagonal Down Left

        elif head.positionX > tail.positionX and head.positionY > tail.positionY:
            tail.update_position(tail.positionX + 1, tail.positionY + 1)
            # Diagonal Down Right


# class for Head and Tail
class RopePart(object):
    def __init__(self, name, positionX, positionY):
        self.name = name
        self.positionX = positionX
        self.positionY = positionY
        self.pastCoords = [tuple([positionX, positionY])]
        # self.path = np.zeros((positionX * 2, positionY * 2))
        # Since array is row column, positionY is first
        # self.path[positionY, positionX] = 1

    def update_position(self, positionX, positionY):
        self.pastCoords.append(tuple([positionX, positionY]))
        # self.path[positionY, positionX] = 1
        self.positionX = positionX
        self.positionY = positionY


# main function
def main(filename):
    input = get_input(filename)

    gridSize = 0
    # head = RopePart("Head", gridSize // 2, gridSize // 2)
    # tail = RopePart("Tail", gridSize // 2, gridSize // 2)

    ropeLength = 10
    rope = []
    for i in range(ropeLength):
        rope.append(RopePart(i, gridSize // 2, gridSize // 2))

    for line in input:
        # head_movement(head, tail, line)
        head_movement_long(rope[0], line, rope)

    # print("Unique Tail Positions: " + str(np.sum(tail.path)))
    # print("Unique Tail Positions: " + str(len(set(tail.pastCoords))))
    print("Unique Tail Positions: " + str(len(set(rope[1].pastCoords))))

    # print("Unique Tail Positions (long version): " + str(np.sum(rope[-1].path)))
    print("Unique Tail Positions (long version): " + str(len(set(rope[-1].pastCoords))))


main("day-9/input.txt")
