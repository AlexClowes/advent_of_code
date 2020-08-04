def run(program, initial_state = (0, 0)):
    registers = dict(zip("ab", initial_state))
    instruction_pointer = 0
    while 0 <= instruction_pointer < len(program):
        line = program[instruction_pointer]
        op = line[:3]
        args = line[4:]
        if op == "hlf":
            registers[args] //= 2
            instruction_pointer += 1
        elif op == "tpl":
            registers[args] *= 3
            instruction_pointer += 1
        elif op == "inc":
            registers[args] += 1
            instruction_pointer += 1
        elif op == "jmp":
            instruction_pointer += int(args)
        elif op == "jie":
            r, offset = args.split(", ")
            if registers[r] % 2 == 0:
                instruction_pointer += int(offset)
            else:
                instruction_pointer += 1
        elif op == "jio":
            r, offset = args.split(", ")
            if registers[r] == 1:
                instruction_pointer += int(offset)
            else:
                instruction_pointer += 1
    return registers["a"], registers["b"]


def main():
    with open("program.txt") as f:
        program = [line.strip() for line in f]
    _, b = run(program)
    print(b)

    _, b = run(program, initial_state=(1, 0))
    print(b)


if __name__ == "__main__":
    main()
