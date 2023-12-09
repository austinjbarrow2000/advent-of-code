import os
import sys
import re


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)


# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data

#     def PrintTree(self):
#         print(self.data)


# def find_node(root, data):
#     if root.data == data:
#         return root
#     elif root.left != None:
#         return find_node(root.left, data)
#     elif root.right != None:
#         return find_node(root.right, data)
#     else:
#         return None


# leaves = []
dict = {}
for i in range(0, len(results)):
    if i == 0:
        instructions = list(results[i])
    elif i == 2:
        results[i] = re.sub(r"[^A-Za-z0-9 ]+", "", results[i])
        list = results[i].split(" ")
        root = list[0]
        dict[list[0]] = (list[2], list[3])
        # root = Node(list[0])
        # left = Node(list[2])
        # right = Node(list[3])
        # root.left = left
        # root.right = right
        # leaves.append(root)
        # leaves.append(left)
        # leaves.append(right)
    elif i >= 3:
        results[i] = re.sub(r"[^A-Za-z0-9 ]+", "", results[i])
        list = results[i].split(" ")
        dict[list[0]] = (list[2], list[3])
        # find_node(root, list[0]).left = Node(list[2])
        # find_node(root, list[0]).right = Node(list[3])

steps = 0
destination = False
# root = "AAA"
# # print(root.left.data)
# while destination == False:
#     for instruction in instructions:
#         print(steps)
#         steps += 1
#         if instruction == "L":
#             root = dict[root][0]
#         elif instruction == "R":
#             root = dict[root][1]

#         if root == "ZZZ":
#             destination = True
#             break

# part 2
rootA = [leaf for leaf in dict.keys() if leaf[2] == "A"]
# print(rootA)

# print(root.left.data)
steps = [0] * len(rootA)
for i in range(0, len(rootA)):
    destination = False
    print(i)
    while destination == False:
        print(i)
        for instruction in instructions:
            # print(instruction)
            # print(steps)
            print(steps)
            print(rootA[i])
            steps[i] += 1
            if instruction == "L":
                rootA[i] = dict[rootA[i]][0]
            elif instruction == "R":
                rootA[i] = dict[rootA[i]][1]

            # print(rootA)
            print(rootA[i])
            if rootA[i][2] == "Z":
                destination = True
                break

print(steps)

from math import gcd

lcm = 1
for i in steps:
    lcm = lcm * i // gcd(lcm, i)
print(lcm)
