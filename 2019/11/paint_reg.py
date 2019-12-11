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
    hull[tuple(pos)] = 1
    while True:
        try:
            hull[tuple(pos)] = c.send(hull[tuple(pos)])
            heading = (2 * next(c) - 1) * rot(heading)
            pos += heading
            next(c)
        except StopIteration:
            break

    min_i = min(k[0] for k in hull.keys())
    max_i = max(k[0] for k in hull.keys()) + 1
    min_j = min(k[1] for k in hull.keys())
    max_j = max(k[1] for k in hull.keys()) + 1
    for i in range(min_i, max_i):
        for j in range(min_j, max_j):
            if (i, j) in hull and hull[i,j] == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()
