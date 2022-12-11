import re

# get input
import os
import sys


def get_input(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        results = f.read().splitlines()
    return results


# monkey class (operation, divisible num, true false throws)

# Efficient Modular Arithmentic, Important property: (a * b) mod m = ((a mod m) * (b mod m)) mod m


class Monkey:
    def __init__(self, items, operation, divisible, true, false):
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.true = true
        self.false = false
        self.inspected = 0

    def inspect(self):
        while len(self.items) > 0:
            self.inspected += 1
            self.items[0] = self.operation(self.items[0])
            self.items[0] = self.items[0] % commonMod
            # self.items[0] = self.items[0] // 3
            if self.items[0] % self.divisible == 0:
                monkeys[self.true].items.append(self.items[0])
                self.items.pop(0)
            else:
                monkeys[self.false].items.append(self.items[0])
                self.items.pop(0)

    def update_items(self, items):
        self.items = items


# next round function
def next_round():
    for monkey in monkeys:
        monkey.inspect()
        # print("Inspection")
        # for monkey in monkeys:
        #     print(monkey.inspected, "MONKEY ITEMS:", monkey.items)


# create operation function
import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}


def create_operation(operation_input):
    operator = ops[operation_input[0]]
    y = operation_input[1]

    if y == "old":

        def operation(x):
            return operator(x, x)

    else:

        def operation(x):
            return operator(x, int(y))

    return operation


def monkey_business():
    inspected = []
    for monkey in monkeys:
        inspected.append(monkey.inspected)
    inspected = sorted(inspected)
    print("Monkey Business", inspected[-2] * inspected[-1])


# main
def main(filename):
    global monkeys, commonMod
    input = get_input(filename)
    while len(input) > 0:
        if "Monkey" in input[0]:
            input.pop(0)
            items = re.findall(r"\d+", input.pop(0))
            operation = create_operation(input.pop(0).split(" ")[6:])
            divisible = re.findall(r"\d+", input.pop(0))
            true = re.findall(r"\d+", input.pop(0))
            false = re.findall(r"\d+", input.pop(0))
            monkeys.append(
                Monkey(
                    [eval(item) for item in items],
                    operation,
                    int(divisible.pop()),
                    int(true.pop()),
                    int(false.pop()),
                )
            )
        else:
            input.pop(0)

    # for monkey in monkeys:
    #     print(monkey.inspected, "MONKEY ITEMS:", monkey.items)

    for monkey in monkeys:
        commonMod *= monkey.divisible

    for i in range(10000):
        next_round()
        print(i)

    monkey_business()


monkeys = []
commonMod = 1
main("input.txt")
