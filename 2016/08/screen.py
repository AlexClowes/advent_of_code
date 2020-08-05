import re

import numpy as np


def display(screen):
    print("\n".join("".join(" #"[x] for x in row) for row in screen))


def main():
    with open("program.txt") as f:
        program = [line.strip() for line in f]

    screen = np.zeros((6, 50), dtype=np.bool)
    rect_pat = r"(\d+)x(\d+)"
    rot_pat = r"=(\d+) by (\d+)"
    for instruction in program:
        if instruction.startswith("rect"):
            width, height = map(int, re.search(rect_pat, instruction).groups())
            screen[:height, :width] = 1
        elif instruction.startswith("rotate row"):
            y, rot = map(int, re.search(rot_pat, instruction).groups())
            screen[y] = np.roll(screen[y], rot)
        elif instruction.startswith("rotate column"):
            x, rot = map(int, re.search(rot_pat, instruction).groups())
            screen[:, x] = np.roll(screen[:, x], rot)
    print(np.sum(screen))
    display(screen)



if __name__ == "__main__":
    main()
