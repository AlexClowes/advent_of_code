from collections import deque

import numpy as np


def main():
    size = 71
    blocked = np.zeros((size, size), dtype=bool)

    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < size - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < size - 1:
            yield i, j + 1

    def can_escape(blocked):
        start, end = (0, 0), (size - 1, size - 1)
        seen = set()
        q = deque([start])
        while q:
            pos = q.popleft()
            if pos == end:
                return True
            if pos in seen:
                continue
            seen.add(pos)
            q.extend(new_pos for new_pos in adj(*pos) if not blocked[new_pos])
        return False

    with open("bytes.txt") as f:
        coords = np.array([list(map(int, line.strip().split(","))) for line in f])

    lo, hi = 0, len(coords)
    while lo < hi:
        mid = (lo + hi) // 2
        blocked[:] = False
        blocked[coords[:mid, 0], coords[:mid, 1]] = True
        if can_escape(blocked):
            lo = mid + 1
        else:
            hi = mid
    print(*coords[lo - 1], sep=",")


if __name__ == "__main__":
    main()
