from collections import deque

import numpy as np


def main():
    with open("heightmap.txt") as f:
        heightmap = np.array([[int(char) for char in line.strip()] for line in f])


    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < heightmap.shape[0] - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < heightmap.shape[1] - 1:
            yield i, j + 1


    def is_low(i, j):
        return all(heightmap[i, j] < heightmap[a] for a in adj(i, j))


    def basin_size(start):
        size = 0
        seen = set()
        q = deque((start,))
        while q:
            pos = q.popleft()
            if pos not in seen:
                size += 1
                seen.add(pos)
                for new_pos in adj(*pos):
                    if heightmap[new_pos] != 9:
                        q.append(new_pos)
        return size


    basin_sizes = [
        basin_size((i, j)) for i, j in np.ndindex(heightmap.shape) if is_low(i, j)
    ]
    print(np.product(sorted(basin_sizes)[-3:]))


if __name__ == "__main__":
    main()
