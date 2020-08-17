from collections import defaultdict
import operator
import re


def main():
    registers = defaultdict(int)
    condition_pat = r"if (\w+) (==|!=|<|>|<=|>=) (-?\d+)"
    op_pat = r"(\w+) (inc|dec) (-?\d+)"
    relations = {
        "==": operator.eq,
        "!=": operator.ne,
        "<": operator.lt,
        ">": operator.gt,
        "<=": operator.le,
        ">=": operator.ge,
    }
    operations = {"inc": operator.add, "dec": operator.sub}
    max_ever = 0
    with open("program.txt") as f:
        for line in f:
            line = line.strip()
            arg1, rel, arg2 = re.search(condition_pat, line).groups()
            if relations[rel](registers[arg1], int(arg2)):
                arg1, op, arg2 = re.search(op_pat, line).groups()
                registers[arg1] = operations[op](registers[arg1], int(arg2))
            max_ever = max(max_ever, max(registers.values()))

    print(max(registers.values()))
    print(max_ever)


if __name__ == "__main__":
    main()
