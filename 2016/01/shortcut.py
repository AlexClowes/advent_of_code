from collections import deque

import numpy as np


def follow(instructions):
    pos = np.array([0, 0])
    headings = deque(np.array([[0, 1], [1, 0], [0, -1], [-1, 0]]))
    for instr in instructions:
        turn = instr[0]
        dist = int(instr[1:])
        if turn == "L":
            headings.rotate(1)
        else:
            headings.rotate(-1)
        pos += dist * headings[0]
    return pos


def manhattan_metric(x, y):
    return abs(x) + abs(y)


def main():
    with open("instructions.txt") as f:
        instructions = f.readline().split(", ")
    pos = follow(instructions)
    print(manhattan_metric(*pos))


if __name__ == "__main__":
    main()
