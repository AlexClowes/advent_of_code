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
    with open("samples.txt") as f:
        lines = [line.strip() for line in f]

    sample_count = 0
    for i in range(0, len(lines), 4):
        registers_before = get_ints(lines[i])
        opcode, a, b, c = get_ints(lines[i + 1])
        registers_after = get_ints(lines[i + 2])
        if len(possible_ops(a, b, c, registers_before, registers_after)) >= 3:
            sample_count += 1
    print(sample_count)


if __name__ == "__main__":
    main()
