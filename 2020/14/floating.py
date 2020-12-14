import re


def apply_mask(mask, loc):
    loc = f"{loc:036b}"
    new_locs = [0]
    for mbit, lbit in zip(mask, loc):
        new_locs = [2 * n for n in new_locs]
        if mbit == "X":
            new_locs += [n + 1 for n in new_locs]
        elif mbit == "1" or lbit == "1":
            new_locs = [n + 1 for n in new_locs]
    return new_locs


def main():
    memory = {}
    with open("instructions.txt") as f:
        for line in f:
            if m := re.match(r"mask = ([X01]+)", line):
                mask = m.group(1)
            elif m := re.match(r"mem\[(\d+)\] = (\d+)", line):
                loc, val = map(int, m.groups())
                for new_loc in apply_mask(mask, loc):
                    memory[new_loc] = val
    print(sum(memory.values()))


if __name__ == "__main__":
    main()
