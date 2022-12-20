import os
import sys
import re
from collections import deque
import numpy as np
from time import sleep as wait
from functools import reduce


def get_input(filename: str) -> list[list[int]]:
    """Get all positive integers from each line and put into arrays by line

    Args:
        filename (str): File name of input file

    Returns:
        list[list[int]]: list of lists of positive integers corresponding to robot costs per blueprint
    """
    with open(os.path.join(sys.path[0], filename), 'r') as f:
        input = f.read().splitlines()
        input = [re.findall(r"\d+", line) for line in input]
        for i, list in enumerate(input):
            input[i] = [int(num) for num in list]
    return input


class BluePrint(object):
    def __init__(self, input_line: list[int], total_time: int):
        """Initialize a new Blueprint with input line and total time, calculating max geodes and quality level

        Args:
            input_line (list[int]): input line of integers correlating to robot costs
            total_time (int): total time given for geode production
        """

        self.id = input_line[0]
        self.ore_robot = input_line[1]
        self.clay_robot = input_line[2]
        self.obsidian_robot = (input_line[3], input_line[4])
        self.geode_robot = (input_line[5], input_line[6])
        self.max_geodes = self.get_max_geodes(total_time)
        self.quality_level = self.get_quality_level()

    def get_max_geodes(self, total_time: int) -> int:
        """ Solve for the maximum geodes produced in given time using Breadth First Search to 
        evaluate all possible production paths, pruning least optimal paths along the way

        Args:
            total_time (int): total time in minutes for geode production

        Returns:
            int: maximum geodes produced in given time
        """

        print("BLUEPRINT", self.id)
        # Initialize queue with initial state [num robots (1 ore), number of resources, 0 time elapsed]
        queue = deque([[np.array([1, 0, 0, 0]), np.array([0, 0, 0, 0]), 0]])
        max_geodes = 0
        time_holder = 0

        while queue:
            # wait(0.5)

            num_robots, num_resources, time_elapsed = queue.popleft()

            # sort queue whenever in new minute
            if time_holder == time_elapsed - 1:
                time_holder += 1
                placeholder_queue = deque([])

                # print('QUEUE BEFORE SORT', queue)
                # sort queue based on robots created
                queue = deque(sorted(queue, key=lambda x: (
                    x[0][3], x[0][2], x[0][1], x[0][0]), reverse=True))
                # print("QUEUE AFTER SORT", queue)

                # only keep top 1000 paths
                for _ in range(1000):
                    if len(queue) > 0:
                        placeholder_queue.append(queue.popleft())

                queue = placeholder_queue

            # check if each robot can be created and add to queue what it would be like if it was created
            # Check the minimum number of specific resource to produce any robot for each robot to create
            # different branches
            if (time_elapsed <= total_time):

                # print path if new max geode found
                if num_resources[3] == max_geodes + 1:
                    print(time_elapsed, max_geodes +
                          1, num_robots, num_resources)
                    # wait(5)

                # always keep track of maximun number of geodes found so far
                max_geodes = max(max_geodes, num_resources[3])

                # Prune if not on pace with max geodes)
                if num_resources[3] != max_geodes:
                    continue

                #print(time_elapsed, max_geodes, num_robots, num_resources)
                time_elapsed += 1

                # ore_robot
                # check if there are resources for ore robot and robots less than max you can spend ore per turn
                if num_resources[0] >= self.ore_robot and \
                        num_robots[0] < max(self.ore_robot, self.clay_robot, self.obsidian_robot[0], self.geode_robot[0]):
                    temp_robots = np.copy(num_robots)
                    temp_resources = np.copy(num_resources)
                    temp_resources = np.add(temp_robots, temp_resources)
                    temp_robots[0] += 1
                    temp_resources[0] -= self.ore_robot
                    queue.append([temp_robots, temp_resources, time_elapsed])

                # clay robot
                # Check if there are resources for clay robot and robots less than max you can
                # spend clay per turn

                if num_resources[0] >= self.clay_robot and num_robots[1] < self.obsidian_robot[1]:
                    temp_robots = np.copy(num_robots)
                    temp_resources = np.copy(num_resources)
                    temp_resources = np.add(temp_robots, temp_resources)
                    temp_robots[1] += 1
                    temp_resources[0] -= self.clay_robot
                    queue.append([temp_robots, temp_resources, time_elapsed])

                # obsidian_robot
                # Check if clay robots, if resources for obsidian robot,
                # and if robots less than max you can spend obsidian per turn

                if num_robots[1] > 0 and num_resources[0] >= self.obsidian_robot[0] and \
                        num_resources[1] >= self.obsidian_robot[1] and num_robots[3] < 5 and \
                        num_robots[2] < self.geode_robot[1]:
                    temp_robots = np.copy(num_robots)
                    temp_resources = np.copy(num_resources)
                    temp_resources = np.add(temp_robots, temp_resources)
                    temp_robots[2] += 1
                    temp_resources[0] -= self.obsidian_robot[0]
                    temp_resources[1] -= self.obsidian_robot[1]
                    queue.append([temp_robots, temp_resources, time_elapsed])

                # geode_robot
                # Check if there are obsidian robots, if there are resources for geode robot

                if num_robots[2] > 0 and num_resources[0] >= self.geode_robot[0] and \
                   num_resources[2] >= self.geode_robot[1]:
                    temp_robots = np.copy(num_robots)
                    temp_resources = np.copy(num_resources)
                    temp_resources = np.add(temp_robots, temp_resources)
                    temp_robots[3] += 1
                    temp_resources[0] -= self.geode_robot[0]
                    temp_resources[2] -= self.geode_robot[1]
                    queue.append([temp_robots, temp_resources, time_elapsed])

                # Only wait for new materials (do not produce a robot) if we are missing
                # a resource and we have a robot that produces it

                # did not produce ore, clay, or obsidian robot due to not having enough ore
                # (+ we have ore robot)
                if (num_resources[0] < max(self.ore_robot, self.clay_robot, self.obsidian_robot[0],
                                           self.geode_robot[0]) and num_robots[0] > 0):
                    num_resources = np.add(num_robots, num_resources)
                    queue.append([num_robots, num_resources, time_elapsed])
                    continue

                # did not produce obsidian robot due to not having enough clay for them (+ we have clay robot)
                if (num_resources[1] < self.obsidian_robot[1] and num_robots[1] > 0):
                    num_resources = np.add(num_robots, num_resources)
                    queue.append([num_robots, num_resources, time_elapsed])
                    continue

                # did not produce obsidian robot due to not having enough obsidian
                # for them (+ we have obsidian robot)
                if (num_resources[2] < self.geode_robot[1] and num_robots[2] > 0):
                    num_resources = np.add(num_robots, num_resources)
                    queue.append([num_robots, num_resources, time_elapsed])
                    continue

        return max_geodes

    def get_quality_level(self) -> int:
        """Get quality level of blueprint (max geodes * id number)

        Returns:
            int: quality level of blueprint
        """
        return self.max_geodes * self.id


def main(filename):
    input = get_input(filename)

    blueprints = []
    quality_levels = []
    max_geodes = []

    total_time = 32  # 24  # how many minutes we have

    # Initialize each blueprint using input and get quality levels and max geodes
    for i, line in enumerate(input):
        blueprints.append(BluePrint(line, total_time))
        quality_levels.append(blueprints[i].quality_level)
        max_geodes.append(blueprints[i].max_geodes)

    print(quality_levels)
    print(sum(quality_levels))
    print(max_geodes)
    print(reduce(lambda x, y: x*y, max_geodes))


main("inputPart2.txt")


# 1129 too low, 1297 not correct, 1321, 1346, 1346 IS CORRECT!!!
# PART 2: 7644 with 300,000, 7644 with 500,000, 7644 with 1000
