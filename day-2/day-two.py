encryption = {
    "A": 0,  # Rock
    "B": 1,  # Paper
    "C": 2,  # Scissors
    "X": 0,  # Rock or Lose
    "Y": 1,  # Paper or Draw
    "Z": 2,  # Scissors or Win
}

# Had to change to


def get_input(filename):
    input_file = open(filename, "r")
    results = input_file.read().splitlines()
    input_file.close()
    return results


def get_score(round, encryption):
    opponentMove = (
        encryption.get(round[0]) + 1
    )  # Had to add plus one, since I needed to reduce by one for score Two
    yourMove = encryption.get(round[1]) + 1
    if opponentMove == yourMove:  # Draw occurred
        return yourMove + 3
    elif opponentMove == yourMove + 1 or opponentMove == yourMove - 2:  # You lost
        return yourMove

    return yourMove + 6  # You won


def get_scoreTwo(round, encryption):
    opponentMove = encryption.get(round[0])
    yourMove = encryption.get(round[1])
    if yourMove == 0:  # Lose must occur
        return (opponentMove + 2) % 3 + 1  # For you to lose, you must have the one -1
    elif yourMove == 1:  # Draw must occur
        return opponentMove + 3 + 1

    return (
        (opponentMove + 1) % 3 + 6 + 1
    )  # Win must occur. For you to win, you must have the one +1


results = get_input("day-two/input.txt")
score = 0
scoreTwo = 0
for round in results:
    round = round.split(" ")
    score += get_score(round, encryption)

for round in results:
    round = round.split(" ")
    scoreTwo += get_scoreTwo(round, encryption)

print(score)
print(scoreTwo)
