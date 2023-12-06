import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

for i in range(0, len(results)):
    if i == 0:
        time = [num for num in results[i].split(" ") if num.isdigit()]
    else:
        distance = [num for num in results[i].split(" ") if num.isdigit()]

time2 = ""
distance2 = ""
for i in range(0, len(time)):
    time2 += time[i]
    distance2 += distance[i]

time2 = int(time2)
distance2 = int(distance2)

win = 0
total = 1
# for i in range(0, len(time)):
#     win = 0
for j in range(0, time2):
    if j * (time2 - j) > distance2:
        win += 1
total = win * total
print(win)
print(total)
