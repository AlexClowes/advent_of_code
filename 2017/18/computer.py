from collections import defaultdict


def run(program):
    registers = defaultdict(int)
    value = lambda x: registers[x] if x.isalpha() else int(x)
    instruction_pointer = 0
    while 0 <= instruction_pointer < len(program):
        op, *args = program[instruction_pointer].split()
        if op == "snd":
            registers["rcv"] = value(args[0])
        elif op == "set":
            registers[args[0]] = value(args[1])
        elif op == "add":
            registers[args[0]] += value(args[1])
        elif op == "mul":
            registers[args[0]] *= value(args[1])
        elif op == "mod":
            registers[args[0]] %= value(args[1])
        elif op == "rcv":
            if value(args[0]) != 0:
                return registers["rcv"]
        elif op == "jgz":
            if value(args[0]):
                instruction_pointer += value(args[1]) - 1
        instruction_pointer += 1


def main():
    with open("program.txt") as f:
        program = [line.strip() for line in f]
    print(run(program))


if __name__ == "__main__":
    main()
