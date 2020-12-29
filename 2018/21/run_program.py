import operator


BIN_OPS = {
    "add": operator.add,
    "mul": operator.mul,
    "ban": operator.and_,
    "bor": operator.or_,
}
RELATIONS = {"gt": operator.gt, "eq": operator.eq}


def execute(op, a, b, registers):
    if op[:3] in BIN_OPS:
        a = registers[a]
        if op[3] == "r":
            b = registers[b]
        return BIN_OPS[op[:3]](a, b)
    if op[:2] in RELATIONS:
        if op[2] == "r":
            a = registers[a]
        if op[3] == "r":
            b = registers[b]
        return int(RELATIONS[op[:2]](a, b))
    if op[:3] == "set":
        if op[3] == "r":
            a = registers[a]
        return a
    raise ValueError(f"Unknown operation {op}")


def get_op_args(line):
    op, *args = line.strip().split()
    return (op,) + tuple(int(a) for a in args)


def main():
    with open("program.txt") as f:
        instr_ptr_binding = int(f.readline().split()[-1])
        program = list(map(get_op_args, f))

    # The program will only terminate if registers[0] == registers[1] on line 28.
    # Since registers[0] is never modified by the program, we just need to find
    # the value of registers[1] the first time we reach line 28 for part 1.

    r1_vals = set()
    registers = [0] * 6
    instr_ptr = 0
    while 0 <= instr_ptr < len(program):
        if instr_ptr == 28:
            break
        registers[instr_ptr_binding] = instr_ptr
        op, a, b, c = program[instr_ptr]
        registers[c] = execute(op, a, b, registers)
        instr_ptr = registers[instr_ptr_binding]
        instr_ptr += 1
    print(registers[1])


if __name__ == "__main__":
    main()
