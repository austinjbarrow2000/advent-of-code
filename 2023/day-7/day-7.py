import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


filename = "./input.txt"
results = get_input(filename)

cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

handsBidRank = []
# bids = []
# rank = []
for line in results:
    inputs = line.split(" ")
    handsBidRank.append([inputs[0], inputs[1], -1, -1])
    # hands.append(inputs[0])
    # bids.append(inputs[1])

for i in range(0, len(handsBidRank)):
    handDict = {}
    input = list(handsBidRank[i][0])
    for card in input:
        handDict[card] = handDict.get(card, 0) + 1
    Jvalue = handDict.get("J", 0)
    handDict["J"] = 0
    handDictValues = list(handDict.values())
    print(handDictValues)
    if 5 in handDict.values() or (Jvalue + max(handDictValues) == 5) or Jvalue == 5:
        handsBidRank[i][2] = 1
    elif 4 in handDict.values() or (Jvalue + max(handDictValues) == 4) or Jvalue == 4:
        handsBidRank[i][2] = 2
    elif (
        (3 in handDict.values() and 2 in handDict.values())
        or (3 in handDict.values() and Jvalue >= 1)
        or (
            handDictValues.count(2) >= 2
            and Jvalue >= 1  # error here regarding 2 in handdictvalues
        )
    ):
        handsBidRank[i][2] = 3
    elif 3 in handDict.values() or (Jvalue + max(handDictValues) == 3) or Jvalue == 3:
        handsBidRank[i][2] = 4
    elif handDictValues.count(2) >= 2 or (2 in handDictValues and Jvalue == 1):
        handsBidRank[i][2] = 5
    elif 2 in handDict.values() or (Jvalue + max(handDictValues) == 2) or Jvalue == 2:
        handsBidRank[i][2] = 6
    else:
        handsBidRank[i][2] = 7
    handDict["J"] = Jvalue


rank = len(handsBidRank)
sortedIndices = []
for j in range(1, 8):
    indices = [i for i in range(len(handsBidRank)) if handsBidRank[i][2] == j]
    # sortedIndices = sorted(indices, key=cards[(list(handsBidRank[indices][0])[0])])
    # for card in range(0, 5, 1):

    sortedIndices = sorted(
        indices,
        key=lambda i: (
            cards[list(handsBidRank[i][0])[0]],
            cards[list(handsBidRank[i][0])[1]],
            cards[list(handsBidRank[i][0])[2]],
            cards[list(handsBidRank[i][0])[3]],
            cards[list(handsBidRank[i][0])[4]],
        ),
        reverse=True,
    )
    print(sortedIndices)
    # sortedIndices = sorted(
    #     indices, key=lambda i: cards[list(handsBidRank[i][0])[0]], reverse=True
    # )
    # print(sortedIndices)

    for index in sortedIndices:
        handsBidRank[index][3] = rank
        rank -= 1

total = 0
for result in handsBidRank:
    total += int(result[1]) * result[3]
    print(
        result[0] + " " + str(result[1]) + " " + str(result[2]) + " " + str(result[3])
    )

print(total)
