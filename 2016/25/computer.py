from itertools import count


def run(program, initial_state=(0, 0, 0, 0)):
    registers = dict(zip("abcd", initial_state))
    evaluate = lambda x: registers[x] if x in registers else int(x)
    program = [[line[:3], line[4:].split()] for line in program]
    instruction_pointer = 0
    while 0 <= instruction_pointer < len(program):
        op, args = program[instruction_pointer]
        if op == "inc":
            registers[args[0]] += 1
        elif op == "dec":
            registers[args[0]] -= 1
        elif op == "cpy":
            if args[1] in registers:
                registers[args[1]] = evaluate(args[0])
        elif op == "jnz":
            if evaluate(args[0]) != 0:
                instruction_pointer += evaluate(args[1]) - 1
        elif op == "out":
            yield evaluate(args[0])
        else:
            raise ValueError(f"Unrecognised instruction {line}")
        instruction_pointer += 1
    return registers["a"]


def main():
    with open("program.txt") as f:
        program = [line.strip() for line in f]

    for a in count(1):
        signal = run(program, initial_state=(a, 0, 0, 0))
        # Assume that if signal is good for 100 iterations, it is good forever
        if all(out == i % 2 for out, i in zip(signal, range(10))):
            print(a)
            break


if __name__ == "__main__":
    main()
