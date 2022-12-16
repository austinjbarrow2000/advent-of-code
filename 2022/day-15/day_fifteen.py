# get input
import os
import sys
import re


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as f:
        input = f.read().splitlines()
        input = [re.findall(r"\-?\d+", line) for line in input]
        # x1, y1, x2, y2 URGHHHH DIDNT INCLUDE OPTIONAL NEGATIVE AT FIRST
    return input

# parse input for sensors and beacons


def calc_sensors_and_beacons(x1, y1, x2, y2, grid, noBeacon, num):
    # global sensors, beacons, nobeacons
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    grid[(x1, y1)] = 'Sensor'
    grid[(x2, y2)] = 'Beacon'
    dist = abs(x1 - x2) + abs(y1 - y2)
    #corners = [(x1-dist, y1), (x1, y1-dist), (x1, y1+dist), (x1+dist, y1)]
    # squarecoords

    # print('yo')
    # print(grid[(2, 10)])
    i = 0
    for x in range(x1-dist, x1):
        for y in range(y1-i, i+1+y1):
            print(x, y)
            if (x, y) not in grid and y == num:
                noBeacon[(x, y)] = 'None'
        i += 1
    for x in range(x1, x1+dist+1):
        for y in range(y1-i, i+1+y1):
            print(x, y)
            if (x, y) not in grid and y == num:
                noBeacon[(x, y)] = 'None'
        i -= 1

    # print(grid)
    # print(len(grid))


def calc_distances(x1, y1, x2, y2, grid, sensors, dist):
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    grid[(x1, y1)] = 'Sensor'
    grid[(x2, y2)] = 'Beacon'
    sensors.append((x1, y1))
    dist.append(abs(x1 - x2) + abs(y1 - y2))
    return sensors, dist
# main function


def check_point(x, y, sensors, dist, grid):
    for i in range(len(sensors)):
        x2, y2 = sensors[i]
        if (x, y) in grid:
            print(grid[(x, y)])
        if abs(x - x2) + abs(y - y2) <= dist[i] and (x, y) not in grid:
            return 1
    return 0


def check_point2(x, y, sensors, dist, grid):
    # print('hi')
    for i in range(len(sensors)):
        x2, y2 = sensors[i]
        # if (x, y) in grid:
        #     print(grid[(x, y)])
        if abs(x - x2) + abs(y - y2) <= dist[i]:  # and (x, y) not in grid:
            return 0
    # if (x, y) in grid:
    #     return 0
    return (x, y)


def main(filename):
    grid = {}
    nobeacon = {}
    num = 2000000
    sensors = []
    dist = []
    # sensors = set()
    # beacons = set()
    # nobeacons = set()
    input = get_input(filename)
    for line in input:
        # print(*line)
        calc_distances(*line, grid, sensors, dist)
        #calc_sensors_and_beacons(*line, grid, nobeacon, num)

    # print(sensors)
    # print(dist)
    # sum = 0
    # for i in range(-15000000, 15000000):
    #     if i % 1000000 == 0:
    #         print(i)
    #     sum += check_point(i, num, sensors, dist, grid)
    # print(sum)

    results = (0, 0)

    # check each spot right outside square of influence of sensor
    for i in range(len(sensors)):
        sensor = sensors[i]
        print(sensor)
        for x in range(sensor[0]-dist[i]-1, sensor[0] + dist[i] + 2):
            if x < 0 or x > 4000000:
                continue
            dx = abs(sensor[0]-x)
            dy = dist[i] + 1 - dx
            for y in (sensor[1] - dy, sensor[1]+dy):
                if y < 0 or y > 4000000:
                    continue
                seen = False
                result = check_point2(x, y, sensors, dist, grid)
                if result != 0:
                    results = result
                    break
    print(results[0] * 4000000 + results[1])


main("input.txt")
