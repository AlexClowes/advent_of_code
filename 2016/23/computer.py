def run(program, initial_state=(0, 0, 0, 0)):
    registers = dict(zip("abcd", initial_state))
    evaluate = lambda x: registers[x] if x in registers else int(x)
    program = [[line[:3], line[4:].split()] for line in program]
    instruction_pointer = 0
    while 0 <= instruction_pointer < len(program):
        op, args = program[instruction_pointer]
        if op == "nop":
            pass
        elif op == "mul":
            registers[args[0]] = evaluate(args[1]) * evaluate(args[2])
        elif op == "inc":
            registers[args[0]] += 1
        elif op == "dec":
            registers[args[0]] -= 1
        elif op == "cpy":
            if args[1] in registers:
                registers[args[1]] = evaluate(args[0])
        elif op == "jnz":
            if evaluate(args[0]) != 0:
                instruction_pointer += evaluate(args[1]) - 1
        elif op == "tgl":
            line_no = instruction_pointer + evaluate(args[0])
            if 0 <= line_no < len(program):
                n_args = len(program[line_no][1])
                if n_args == 1:
                    new_op = "inc" if program[line_no][0] != "inc" else "dec"
                elif n_args == 2:
                    new_op = "jnz" if program[line_no][0] != "jnz" else "cpy"
                else:
                    raise ValueError(f"Unable to toggle operation with {n_args} arguments")
                program[line_no][0] = new_op
        else:
            raise ValueError(f"Unrecognised instruction {line}")
        instruction_pointer += 1
    return registers["a"]


def main():
    with open("program.txt") as f:
        program = [line.strip() for line in f]

    # Optimise program by hand
    program[4:10] = [
        "mul a b d",
        "cpy 0 c",
        "cpy 0 d",
        "nop",
        "nop",
        "nop",
    ]

    print(run(program[:], initial_state=(7, 0, 0, 0)))
    print(run(program[:], initial_state=(12, 0, 0, 0)))


if __name__ == "__main__":
    main()
