def get_input(filename):
    file = open(filename, "r")
    result = file.read().splitlines()
    return result


input = get_input("day-6/input.txt")

input = list(input[0])
marker = []

processed = 0
while len(set(marker)) != 4:
    if len(marker) == 4:
        marker.pop(0)
    marker.append(input.pop(0))
    processed += 1
print(processed)

input = get_input("day-6/input.txt")
input = list(input[0])
marker = []

processed = 0
while len(set(marker)) != 14:
    if len(marker) == 14:
        marker.pop(0)
    marker.append(input.pop(0))
    processed += 1

print(processed)
