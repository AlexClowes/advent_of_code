from collections import deque
from functools import reduce
from operator import xor

import numpy as np


class CircList:
    def __init__(self, n):
        self.n = n
        self.vals = list(range(n))

    def __getitem__(self, idx):
        return self.vals[idx % self.n]

    def __setitem__(self, idx, val):
        self.vals[idx % self.n] = val


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]


def knot_hash(string):
    lengths = [ord(c) for c in string] + [17, 31, 73, 47, 23]

    pos = 0
    skip = 0
    cl = CircList(256)
    for _ in range(64):
        for l in lengths:
            for i in range(l // 2):
                swap(cl, pos + i, pos + l - i - 1)
            pos += l + skip
            skip += 1
    sparse_hash = cl.vals

    dense_hash = [reduce(xor, sparse_hash[i*16:(i+1)*16]) for i in range(16)]

    return "".join(format(n, "08b") for n in dense_hash)


def gen_grid(key_string):
    grid = np.zeros((128, 128), dtype=np.bool)
    for i in range(128):
        h = knot_hash(key_string + "-" + str(i))
        for j, c in enumerate(h, 0):
            grid[i, j] = (c == "1")
    return grid


def adj(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


def count_regions(grid):
    region_count = 0
    region_map = np.zeros_like(grid, dtype=np.int32)

    def adj(x, y):
        if x > 0:
            yield x - 1, y
        if x < grid.shape[0] - 1:
            yield x + 1, y
        if y > 0:
            yield x, y - 1
        if y < grid.shape[1] - 1:
            yield x, y + 1

    def label_region(start):
        q = deque((start,))
        while q:
            pos = q.popleft()
            region_map[pos] = region_count
            for new_pos in adj(*pos):
                if grid[new_pos] and region_map[new_pos] == 0:
                    q.append(new_pos)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[0]):
            if region_map[i, j] == 0 and grid[i, j]:
                region_count += 1
                label_region((i, j))

    return region_count


def main():
    key_string = "jxqlasbh"
    grid = gen_grid(key_string)

    print(np.sum(grid))
    print(count_regions(grid))


if __name__ == "__main__":
    main()
