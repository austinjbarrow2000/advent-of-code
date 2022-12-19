import os
import sys
from collections import deque


# get input function
def get_input(filename):
    """Open the given file and return the list of lines split into x,y,z coordinates for the droplet

    Args:
        filename (str): file name of the input 

    Returns:
        list(str): list of strings containing the coordinates of the droplet
    """
    with open(os.path.join(sys.path[0], filename), 'r') as f:
        input = f.read().splitlines()
        input = [line.split(',') for line in input]
    return input


# droplet class
class Droplet(object):
    def __init__(self, coord_lines):
        """Initialize droplet by storing input of strings, parseing the input into dictionary of coords,
        using the coords to calculate the droplet bounds, and then calculating the surface area

        Args:
            coord_lines list(str): list of strings that contain the coordinates of the droplet
        """
        self.coord_lines = coord_lines
        self.cube_coords = self.parse_coord_lines()
        self.circle_bounds = self.get_circle_bounds()
        self.surface_area = self.get_surface_area()

    def parse_coord_lines(self) -> dict[int, int, int]:
        """Parse given input into dictionary indicating coordinates of the droplet

        Returns:
            dict[int,int,int]: dictionary of all coordinates of the droplet
        """
        cube_coords = {}
        for coord in self.coord_lines:
            cube_coords[(int(coord[0]), int(coord[1]), int(coord[2]))] = 'D'
        return cube_coords

    def get_surface_area(self) -> int:
        """Calculate surface area of the droplet exposed to the elements 

        Returns:
            int: number of surfaces exposed to the elements
        """
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
        return surface_area

    def get_circle_bounds(self) -> list[int]:
        """Calculate the bounds of the cube encapsulating the droplet given the droplet coordinates

        Returns:
            list[int]: bounds of the cube encapsulating the droplet (max X, max Y, max Z, minX, minY, minZ)
        """
        maxX = maxY = maxZ = 0
        minX = minY = minZ = 10000
        for key in self.cube_coords.keys():
            maxX = max(key[0], maxX)
            maxY = max(key[1], maxY)
            maxZ = max(key[2], maxZ)
            minX = min(key[0], minX)
            minY = min(key[1], minY)
            minZ = min(key[2], minZ)
        bounds = [minX, minY, minZ, maxX, maxY, maxZ]
        return bounds

    def bfs(self, coord: list[int]) -> bool:
        """BFS function to check if droplet cube neighbor has access outside of droplet. Using the neighbors 
        coordinates, adds all of their neighbors to the queue and visited, adds all of those neighbors
        recursively (if not visited), until one of their coordinates outside of circle bounds or neighbors
        run out.

        Args:
            coord (list[int]): coordinates of droplet cube neighbor  

        Returns:
            bool: True/false if given coordinate has access outside of droplet
        """

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


def main(filename: str):
    """ Get filename, make droplet from file and print surface area

    Args:
        filename (str): File name of the input file
    """
    input = get_input(filename)
    droplet = Droplet(input)
    print(droplet.surface_area)


main('input.txt')
