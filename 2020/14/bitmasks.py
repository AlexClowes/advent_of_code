import re


def apply_mask(mask, val):
    val = f"{val:036b}"
    ret = 0
    for mbit, vbit in zip(mask, val):
        ret *= 2
        if mbit == "X":
            ret += int(vbit)
        else:
            ret += int(mbit)
    return ret


def main():
    memory = {}
    with open("instructions.txt") as f:
        for line in f:
            if m := re.match(r"mask = ([X01]+)", line):
                mask = m.group(1)
            elif m := re.match(r"mem\[(\d+)\] = (\d+)", line):
                loc, val = map(int, m.groups())
                memory[loc] = apply_mask(mask, val)
    print(sum(memory.values()))


if __name__ == "__main__":
    main()
