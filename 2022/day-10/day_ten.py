# get input function
import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


# instruction and cycle function
def check_cycle():
    crtRow.append("#") if len(crtRow) in sprite else crtRow.append(".")

    if cycles in [20, 60, 100, 140, 180, 220]:
        signal_strengths.append(register * cycles)


def print_crtRow():
    for _ in range(40):
        if len(crtRow) > 0:
            print(crtRow.pop(0), end="")
    print("", end="\n")


def main():
    input = get_input("input.txt")

    global cycles, register, signal_strengths, crtRow, sprite

    cycles = 0
    register = 1
    signal_strengths = []
    crtRow = []
    sprite = [register - 1, register, register + 1]

    for line in input:
        if len(crtRow) == 40:
            print_crtRow()

        if "noop" in line:
            cycles += 1
            check_cycle()
        else:
            _, num = line.split(" ")
            cycles += 1
            check_cycle()
            cycles += 1
            check_cycle()
            register += int(num)
            sprite = [register - 1, register, register + 1]

    print_crtRow()
    print(sum(signal_strengths))


main()
