import re

import numpy as np


def apply_instruction(lights, instruction):
    search_pat = r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)"
    instr, x1, y1, x2, y2 = re.match(search_pat, instruction).groups()

    affected_area = (slice(int(x1), int(x2) + 1), slice(int(y1), int(y2) + 1))

    if instr == "turn on":
        lights[affected_area] += 1
    elif instr == "turn off":
        lights[affected_area] -= 1
        lights[lights < 0] = 0
    elif instr == "toggle":
        lights[affected_area] += 2
    else:
        raise ValueError(f"Unrecognised instruction {instr}")


def main():
    lights = np.zeros((1000, 1000), dtype=np.int32)
    with open("instructions.txt") as f:
        for instruction in f:
            apply_instruction(lights, instruction)
    print(np.sum(lights))


if __name__ == "__main__":
    main()
