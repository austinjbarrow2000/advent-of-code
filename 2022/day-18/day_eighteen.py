import os
import sys
from collections import deque


# get input function
def get_input(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as f:
        input = f.read().splitlines()
        input = [line.split(',') for line in input]
    return input


# droplet class
class Droplet(object):
    def __init__(self, coord_lines):
        self.coord_lines = coord_lines
        self.cube_coords = self.parse_coord_lines()
        self.circle_bounds = self.get_circle_bounds()
        self.surface_area = self.get_surface_area()

    def parse_coord_lines(self):
        cube_coords = {}
        for coord in self.coord_lines:
            cube_coords[(int(coord[0]), int(coord[1]), int(coord[2]))] = 'D'
        return cube_coords

    def get_surface_area(self):
        neighbors = [(0, 0, 1), (0, 1, 0), (1, 0, 0),
                     (0, 0, -1), (0, -1, 0), (-1, 0, 0)]

        surface_area = 0
        for coord in self.cube_coords.keys():
            print(coord)
            for neighbor in neighbors:
                dx, dy, dz = neighbor
                # check if neighbor has a cube and that there are no cubes further (using x y or z pos)
                neighbor_coord = (
                    coord[0] + dx, coord[1] + dy, coord[2] + dz)
                if neighbor_coord not in self.cube_coords:
                    # check if the neighbor has access to the outside of the sphere
                    if self.bfs(neighbor_coord):
                        surface_area += 1
        return surface_area  # surface_area

    # get the bounds of the cube around the circle (max X, maxY, maxZ, minX, minY, minZ)
    def get_circle_bounds(self):
        maxX = maxY = maxZ = 0
        minX = minY = minZ = 10000
        for key in self.cube_coords.keys():
            if key[0] > maxX:
                maxX = key[0]
            if key[1] > maxY:
                maxY = key[1]
            if key[2] > maxZ:
                maxZ = key[2]
            if key[0] < minX:
                minX = key[0]
            if key[1] < minY:
                minY = key[1]
            if key[2] < minZ:
                minZ = key[2]
        bounds = [minX, minY, minZ, maxX, maxY, maxZ]
        return bounds

    # BFS function
    # get neighbors of coord, add them to the queue and visited, check if coord outside of bounds of circle

    def bfs(self, coord):
        neighbors = [(0, 0, 1), (0, 1, 0), (1, 0, 0),
                     (0, 0, -1), (0, -1, 0), (-1, 0, 0)]
        visited = []
        queue = deque([coord])

        while queue:
            coord = queue.popleft()
            for neighbor in neighbors:
                dx, dy, dz = neighbor
                neighbor_coord = (coord[0] + dx, coord[1] + dy, coord[2] + dz)
                if neighbor_coord not in self.cube_coords and neighbor_coord not in visited:
                    queue.append(neighbor_coord)
                    visited.append(neighbor_coord)

            minX, minY, minZ, maxX, maxY, maxZ = self.circle_bounds

            if coord[0] > maxX or coord[1] > maxY or coord[2] > maxZ or coord[0] < minX or coord[1] < minY or coord[2] < minZ:
                return True
        return False


# main function
def main(filename):
    input = get_input(filename)
    droplet = Droplet(input)
    print(droplet.surface_area)


main('input.txt')
