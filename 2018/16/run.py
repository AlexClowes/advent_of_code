import operator
import re


bin_ops = {
    "add": operator.add,
    "mul": operator.mul,
    "ban": operator.and_,
    "bor": operator.or_,
}
relations = {"gt": operator.gt, "eq": operator.eq}
all_ops = {
    "addi",
    "addr",
    "muli",
    "mulr",
    "bani",
    "banr",
    "bori",
    "borr",
    "seti",
    "setr",
    "gtir",
    "gtri",
    "gtrr",
    "eqir",
    "eqri",
    "eqrr",
}


def execute(op, a, b, registers):
    if op[:3] in bin_ops:
        a = registers[a]
        if op[3] == "r":
            b = registers[b]
        return bin_ops[op[:3]](a, b)
    if op[:2] in relations:
        if op[2] == "r":
            a = registers[a]
        if op[3] == "r":
            b = registers[b]
        return int(relations[op[:2]](a, b))
    if op[:3] == "set":
        if op[3] == "r":
            a = registers[a]
        return a
    raise ValueError(f"Unknown operation {op}")


def get_ints(line):
    return [int(n) for n in re.findall(r"\d+", line)]


def possible_ops(a, b, c, registers_before, registers_after):
    ret = set()
    for op in all_ops:
        if execute(op, a, b, registers_before) == registers_after[c]:
            ret.add(op)
    return ret


def main():
    # Use samples to find opcode corresponding to each operation
    with open("samples.txt") as f:
        lines = [line.strip() for line in f]

    # Get all possible operations for each opcode
    possibilities = {opcode: set(all_ops) for opcode in range(16)}
    for i in range(0, len(lines), 4):
        registers_before = get_ints(lines[i])
        opcode, a, b, c = get_ints(lines[i + 1])
        registers_after = get_ints(lines[i + 2])
        possibilities[opcode] &= possible_ops(a, b, c, registers_before, registers_after)

    # Narrow down possible operations to just one per opcode
    op_map = {}
    while possibilities:
        for opcode, ops in possibilities.items():
            if len(ops) == 1:
                break
        op = ops.pop()
        op_map[opcode] = op
        del possibilities[opcode]
        for ops in possibilities.values():
            ops -= {op}

    # Run program
    registers = [0] * 4
    with open("program.txt") as f:
        for line in f:
            opcode, a, b, c = get_ints(line)
            registers[c] = execute(op_map[opcode], a, b, registers)
    print(registers[0])


if __name__ == "__main__":
    main()
