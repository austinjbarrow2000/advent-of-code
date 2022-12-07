class Directory(object):
    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.children = []
        self.parent = parent

    def addChild(self, obj):
        self.children.append(obj)


class File(object):
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


def get_input(filename):
    file = open(filename, "r")
    results = file.read().splitlines()
    return results


def merge(arr_one, arr_two):
    results = []
    while len(arr_one) > 0 and len(arr_two) > 0:
        if arr_one[0].size < arr_two[0].size:
            results.append(arr_one.pop(0))
        else:
            results.append(arr_two.pop(0))
    while len(arr_one) > 0:
        results.append(arr_one.pop(0))
    while len(arr_two) > 0:
        results.append(arr_two.pop(0))
    return results


def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    arr_one = mergesort(arr[:mid])
    arr_two = mergesort(arr[mid:])
    arr = merge(arr_one, arr_two)
    return arr


input = get_input("day-7/input.txt")
directories = []
home = Directory("/", None)
directories.append(home)
current_dir = home
input.pop(0)

while len(input) > 0:
    line = input.pop(0)
    if "cd" in line:
        if ".." in line:
            current_dir = current_dir.parent
        elif "/" in line:
            current_dir = home
        else:
            name = line[5:]
            for child in current_dir.children:
                if name == child.name:
                    current_dir = child
    elif "ls" in line:
        while len(input) > 0 and "$" not in input[0]:
            do = 1
            objType, name = input.pop(0).split(" ")
            for child in current_dir.children:
                if name == child.name:
                    do = 0
            if do:
                if objType == "dir":
                    directories.append(Directory(name, current_dir))
                    current_dir.addChild(directories[-1])
                else:
                    current_dir.addChild(File(name, objType))

directories2 = []
directories2.append(home)


def calc_size(directory):
    for children in directory.children:
        # print(children.name, end=" ")
        if isinstance(children, Directory):
            directories2.append(children)
            directory.size += calc_size(children)
        else:
            directory.size += children.size
    return directory.size


# for child in home.children:
#     print(child.name, end=" ")

home.size = calc_size(home)
# print(home.size)

sum = 0
for dir in directories:
    print(str(dir.name) + ": " + str(dir.size))
    if dir.size <= 100000:
        sum += dir.size
print(sum)

# print("DIRECTORIES")
# for dir in directories:
#     print(dir.name, end=" ")
# print("DIRECTORIES2")
# for dir in directories2:
#     print(dir.name, end=" ")

directories = mergesort(directories)
available = 70000000 - home.size
neededSpace = 30000000 - available
for child in directories:
    if child.size >= neededSpace:
        print(child.size)
        break
