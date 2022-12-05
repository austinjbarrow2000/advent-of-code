def get_input(filename):
    input = open(filename, "r")
    result = input.read().splitlines()
    return result


pairs = get_input("day-4/input.txt")

reconsider = 0
overlap = 0

for pair in pairs:
    pair = pair.split(",")
    elfOne = pair[0].split("-")
    elfTwo = pair[1].split("-")
    print(str(elfOne) + " " + str(elfTwo) + " " + str(reconsider))
    if int(elfOne[0]) <= int(elfTwo[1]) and int(elfTwo[0]) <= int(elfOne[1]):
        overlap += 1

    if (int(elfOne[0]) >= int(elfTwo[0]) and int(elfOne[1]) <= int(elfTwo[1])) or (
        int(elfTwo[0]) >= int(elfOne[0]) and int(elfTwo[1]) <= int(elfOne[1])
    ):
        reconsider += 1

print(reconsider)
print(overlap)
