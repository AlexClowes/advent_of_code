from collections import deque

import numpy as np


def main():
    with open("heightmap.txt") as f:
        elevation = np.array(
            [[ord(char) - ord("a") for char in line.strip()] for line in f]
        )

    # Set S to a, get end
    for pos, val in np.ndenumerate(elevation):
        if val == ord("S") - ord("a"):
            elevation[pos] = 0
        elif val == ord("E") - ord("a"):
            end = pos
            elevation[end] = 25

    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < elevation.shape[0] - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < elevation.shape[1] - 1:
            yield i, j + 1

    seen = set()
    q = deque([(end, 0)])
    while q:
        pos, steps = q.popleft()
        if elevation[pos] == 0:
            break
        if pos in seen:
            continue
        seen.add(pos)
        for new_pos in adj(*pos):
            if elevation[pos] <= elevation[new_pos] + 1:
                q.append((new_pos, steps + 1))

    print(steps)


if __name__ == "__main__":
    main()
