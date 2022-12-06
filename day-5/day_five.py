def get_input(filename):
    file = open(filename, "r")
    result = file.read().splitlines()
    return result


def convert_input(input):
    crate_input = []
    instruction_input = []

    for line in input:
        if "[" in line:
            line = line.replace("]     ", "] [ ] ")
            line = line.replace("    ", "[ ] ")
            crate_input.append(line.replace("[ ]", "None"))
        elif "move" in line:
            instruction_input.append(line)

    return crate_input, instruction_input


def create_stacks(crate_input):
    crates = []
    stacks = [[] for i in range(((len(crate_input[0])) // 4) - 1)]
    for input in crate_input:
        crates = input.split(" ")
        for i in range(len(crates)):
            if crates[i] != "None":
                stacks[i].append(crates[i])
    return stacks


def execute_instructions1(stacks, instruction_input):
    for instruction in instruction_input:
        instruction = [int(s) for s in instruction.split() if s.isdigit()]
        for i in range(instruction[0]):
            stacks[instruction[2] - 1].insert(0, stacks[instruction[1] - 1].pop(0))
    return stacks


def execute_instructions2(stacks, instruction_input):
    for instruction in instruction_input:
        instruction = [int(s) for s in instruction.split() if s.isdigit()]
        carrying = []
        for i in range(instruction[0]):
            carrying.insert(0, stacks[instruction[1] - 1].pop(0))
        for i in range(len(carrying)):
            stacks[instruction[2] - 1].insert(0, carrying.pop(0))
    return stacks


input = get_input("day-5/input.txt")

crate_input, instruction_input = convert_input(input)
stacks = create_stacks(crate_input)
stacksOne = execute_instructions1(stacks, instruction_input)
stacks = create_stacks(crate_input)
stacksTwo = execute_instructions2(stacks, instruction_input)

print("STACK ONE")
for stack in stacksOne:
    print(stack)

print("STACK TWO")
for stack in stacksTwo:
    print(stack)
