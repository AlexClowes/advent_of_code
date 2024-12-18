from collections import deque
from itertools import islice

import numpy as np


def main():
    size = 71
    blocked = np.zeros((size, size), dtype=bool)
    with open("bytes.txt") as f:
        for line in islice(f, 1024):
            x, y = map(int, line.strip().split(","))
            blocked[x, y] = True

    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < size - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < size - 1:
            yield i, j + 1

    start, end = (0, 0), (size - 1, size - 1)
    seen = set()
    q = deque([(start, 0)])
    while q:
        pos, steps = q.popleft()
        if pos == end:
            print(steps)
            return
        if pos in seen:
            continue
        seen.add(pos)
        q.extend(
            (new_pos, steps + 1)
            for new_pos in adj(*pos)
            if not blocked[new_pos]
        )


if __name__ == "__main__":
    main()
