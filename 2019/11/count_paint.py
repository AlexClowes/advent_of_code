from collections import defaultdict

import numpy as np

from computer import int_code_computer


def rot(heading):
    return np.array([heading[1], -heading[0]])


def main():
    with open("program.txt") as f:
        program = map(int, f.readline().strip().split(","))

    c = int_code_computer(program)

    hull = defaultdict(int)
    pos = np.array([0, 0])
    heading = np.array([-1, 0])
    while True:
        try:
            hull[tuple(pos)] = c.send(hull[tuple(pos)])
            heading = (2 * next(c) - 1) * rot(heading)
            pos += heading
            next(c)
        except StopIteration:
            break
    print(len(hull))


if __name__ == "__main__":
    main()
