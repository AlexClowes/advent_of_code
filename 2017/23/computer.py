from collections import defaultdict


def run(program, initial_state=(0,) * 8):
    mul_count = 0
    registers = dict(zip("abcdefgh", initial_state))
    value = lambda x: registers[x] if x.isalpha() else int(x)
    instruction_pointer = 0
    while 0 <= instruction_pointer < len(program):
        op , *args = program[instruction_pointer].split()
        if op == "set":
            registers[args[0]] = value(args[1])
        elif op == "sub":
            registers[args[0]] -= value(args[1])
        elif op == "mul":
            registers[args[0]] *= value(args[1])
            mul_count += 1
        elif op == "jnz":
            if value(args[0]) != 0:
                instruction_pointer += value(args[1]) - 1
        instruction_pointer += 1

    return mul_count


def main():
    with open("program.txt") as f:
        program = [line.strip() for line in f]
    print(run(program))


if __name__ == "__main__":
    main()
