import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)


def map(source, destination):
    for i in range(0, len(source)):
        if source[i][0] >= nums[1] and source[i][0] < nums[1] + nums[2]:
            if source[i][1] < nums[1] + nums[2]:
                # replace whole range, complete overlap
                # print(source[i][0])

                destination.append(
                    (
                        source[i][0] - nums[1] + nums[0],
                        source[i][1] - nums[1] + nums[0],
                    )
                )
                source[i] = (-1, -1)

                # print("source1: ", source)
                # print(destination)
            else:
                destination.append(
                    (source[i][0] - nums[1] + nums[0], nums[0] + nums[2] - 1)
                )
                source[i] = (nums[1] + nums[2], source[i][1])
                # replace partial range, stops before top range
                # print("source2: ", source)
                # print(destination)
        elif source[i][0] < nums[1] and source[i][1] > nums[1] + nums[2]:
            # replace partial range, starts before bottom range and ends after top range
            source.append((nums[1] + nums[2], source[i][1]))

            destination.append((nums[0], nums[0] + nums[2] - 1))
            source[i] = (source[i][0], nums[1] - 1)

            # print("source3: ", source)
            # print(destination)
        elif source[i][1] < nums[1] + nums[2] and source[i][1] > nums[1]:
            # replace partial range, starts after bottom range
            destination.append((nums[0], source[i][1] - nums[1] + nums[0]))

            source[i] = (source[i][0], nums[1] - 1)
            # print("source4: ", source)
            # print(destination)


s2s = []
s2f = []
f2w = []
w2l = []
l2t = []
t2h = []
h2l = []

s2sAdd = []
s2fAdd = []
f2wAdd = []
w2lAdd = []
l2tAdd = []
t2hAdd = []
h2lAdd = []

seeds = []

mode = 0

for line in results:
    if "seeds:" in line:
        seeds1 = [int(num) for num in line.split(" ") if num.isdigit()]
        for i in range(0, len(seeds1), 2):
            seeds.append((seeds1[i], seeds1[i] + seeds1[i + 1] - 1))
            # for j in range(seeds1[i], seeds1[i] + seeds1[i + 1]):
            #     seeds[j] = j

        # print("hi")
        # print(len(seeds))
        # print(seeds)

        continue
    elif "seed-to-soil map:" in line:
        mode = 1
        # for key in seeds.keys():
        #     s2s[seeds[key]] = seeds[key]
        continue
    elif "soil-to-fertilizer map:" in line:
        mode = 2
        for seed in seeds:
            if seed != (-1, -1):
                s2s.append(seed)
        # print("s2s:", s2s)

        # for key in s2s.keys():
        #     s2f[s2s[key]] = s2s[key]
        continue
    elif "fertilizer-to-water map:" in line:
        mode = 3
        for key in s2s:
            if key != (-1, -1):
                s2f.append(key)
        # print("s2f:", s2f)

        # for key in s2f.keys():
        #     f2w[s2f[key]] = s2f[key]
        # print(f2w)
        continue
    elif "water-to-light map:" in line:
        mode = 4
        for key in s2f:
            if key != (-1, -1):
                f2w.append(key)
        # print("f2w:", f2w)

        # for key in f2w.keys():
        #     w2l[f2w[key]] = f2w[key]
        # print("w2l")
        # print(w2l)
        continue
    elif "light-to-temperature map:" in line:
        mode = 5
        for key in f2w:
            if key != (-1, -1):
                w2l.append(key)
        # print("w2l:", w2l)

        # for key in w2l.keys():
        #     l2t[w2l[key]] = w2l[key]
        # print(l2t)
        continue
    elif "temperature-to-humidity map:" in line:
        mode = 6
        for key in w2l:
            if key != (-1, -1):
                l2t.append(key)
        # print("l2t:", l2t)

        # for key in l2t.keys():
        #     t2h[l2t[key]] = l2t[key]
        # print(t2h)
        continue
    elif "humidity-to-location map:" in line:
        mode = 7
        for key in l2t:
            if key != (-1, -1):
                t2h.append(key)
        # print("h2l:", h2l)

        # for key in t2h.keys():
        #     h2l[t2h[key]] = t2h[key]
        # print(h2l)
        continue

    if line == "":
        continue
    nums = [int(num) for num in line.split(" ") if num.isdigit()]
    # for key in seeds.keys():
    #     if mode == 1:
    #         if key >= nums[1] and key < nums[1] + nums[2]:
    #             s2s[i] = key - nums[1] + nums[0]
    #     elif mode == 2:
    #         if s2s[i] >= nums[1] and s2s[i] < nums[1] + nums[2]:
    #             s2f[i] = s2s[i] - nums[1] + nums[0]
    #     elif mode == 3:
    #         if s2f[i] >= nums[1] and s2f[i] < nums[1] + nums[2]:
    #             f2w[i] = s2f[i] - nums[1] + nums[0]
    #     elif mode == 4:
    #         if f2w[i] >= nums[1] and f2w[i] < nums[1] + nums[2]:
    #             w2l[i] = f2w[i] - nums[1] + nums[0]
    #     elif mode == 5:
    #         if w2l[i] >= nums[1] and w2l[i] < nums[1] + nums[2]:
    #             l2t[i] = w2l[i] - nums[1] + nums[0]
    #     elif mode == 6:
    #         if l2t[i] >= nums[1] and l2t[i] < nums[1] + nums[2]:
    #             t2h[i] = l2t[i] - nums[1] + nums[0]
    #     elif mode == 7:
    #         if t2h[i] >= nums[1] and t2h[i] < nums[1] + nums[2]:
    #             h2l[i] = t2h[i] - nums[1] + nums[0]

    if mode == 1:
        map(seeds, s2s)

        # else:
        #     # no overlap
        # s2s.append((s2s[i][0], s2s[i][1]))
        # for key in seeds.keys():
        #     if key >= nums[1] and key < nums[1] + nums[2]:
        #         s2s[seeds[key]] = key - nums[1] + nums[0]
    elif mode == 2:
        map(s2s, s2f)

        # for key in s2s.keys():
        #     if s2s[key] >= nums[1] and s2s[key] < nums[1] + nums[2]:
        #         s2f[s2s[key]] = s2s[key] - nums[1] + nums[0]
        # if s2s[i] >= nums[1] and s2s[i] < nums[1] + nums[2]:
        #     s2f[i] = s2s[i] - nums[1] + nums[0]
    elif mode == 3:
        map(s2f, f2w)

        # for key in s2f.keys():
        #     if s2f[key] >= nums[1] and s2f[key] < nums[1] + nums[2]:
        #         f2w[s2f[key]] = s2f[key] - nums[1] + nums[0]
        # if s2f[i] >= nums[1] and s2f[i] < nums[1] + nums[2]:
        #     f2w[i] = s2f[i] - nums[1] + nums[0]
    elif mode == 4:
        map(f2w, w2l)

        # for key in f2w.keys():
        #     if f2w[key] >= nums[1] and f2w[key] < nums[1] + nums[2]:
        #         w2l[f2w[key]] = f2w[key] - nums[1] + nums[0]
        # if f2w[i] >= nums[1] and f2w[i] < nums[1] + nums[2]:
        #     w2l[i] = f2w[i] - nums[1] + nums[0]
    elif mode == 5:
        map(w2l, l2t)

        # for key in w2l.keys():
        #     if w2l[key] >= nums[1] and w2l[key] < nums[1] + nums[2]:
        #         l2t[w2l[key]] = w2l[key] - nums[1] + nums[0]
        # if w2l[i] >= nums[1] and w2l[i] < nums[1] + nums[2]:
        #     l2t[i] = w2l[i] - nums[1] + nums[0]
    elif mode == 6:
        map(l2t, t2h)

        # for key in l2t.keys():
        #     if l2t[key] >= nums[1] and l2t[key] < nums[1] + nums[2]:
        #         t2h[l2t[key]] = l2t[key] - nums[1] + nums[0]
        # if l2t[i] >= nums[1] and l2t[i] < nums[1] + nums[2]:
        #     t2h[i] = l2t[i] - nums[1] + nums[0]
    elif mode == 7:
        map(t2h, h2l)

        # for key in t2h.keys():
        #     if t2h[key] >= nums[1] and t2h[key] < nums[1] + nums[2]:
        #         h2l[t2h[key]] = t2h[key] - nums[1] + nums[0]
        # if t2h[i] >= nums[1] and t2h[i] < nums[1] + nums[2]:
        #     h2l[i] = t2h[i] - nums[1] + nums[0]


# minLocation = 1000000
# print(s2s, s2f, f2w, w2l, l2t, t2h, h2l)
# for num in seeds:
#     soil = s2s.get(num, num)
#     fertilizer = s2f.get(soil, soil)
#     water = f2w.get(fertilizer, fertilizer)
#     light = w2l.get(water, water)
#     temperature = l2t.get(light, light)
#     humidity = t2h.get(temperature, temperature)
#     location = h2l.get(humidity, humidity)

#     if location < minLocation:
#         minLocation = location
# print("final")
# print(
#     seeds,
#     "\n",
#     s2s,
#     "\n",  # s2f, "\n", f2w, "\n", w2l, "\n", l2t, "\n", t2h, "\n", h2l
# )
for key in t2h:
    if key != (-1, -1):
        h2l.append(key)
# print(h2l)
print(min(h2l))
# print(min(h2l.items(), key=lambda x: x[1]))
