import numpy as np


def str2tup(string):
    return tuple(tuple(".#".find(c) for c in row) for row in string.split("/"))


def reflect(grid):
    return tuple(tuple(reversed(row)) for row in grid)


def rot(grid):
    size = len(grid)
    return tuple(tuple(grid[size - 1 - i][j] for i in range(size)) for j in range(size))


def gen_perms(grid):
    for _ in range(4):
        yield grid
        yield reflect(grid)
        grid = rot(grid)


def split(grid, n):
    size = len(grid)
    for i in range(size // n):
        for j in range(size // n):
            yield tuple(
                tuple(grid[i * n + k][j * n + l] for l in range(n)) for k in range(n)
            )


def merge(grids, size):
    # Can this be done with another tuple comprehension?
    ret = np.zeros((size, size), dtype=np.bool)
    for idx, grid in enumerate(grids):
        grid_size = len(grid)
        i, j = divmod(idx, size // grid_size)
        ret[
            i * grid_size : (i + 1) * grid_size, j * grid_size : (j + 1) * grid_size
        ] = np.array(grid)
    return tuple(tuple(row) for row in ret)


def advance(grid, rules):
    size = len(grid)
    small_grid_size = 2 if size % 2 == 0 else 3
    small_grids = split(grid, small_grid_size)
    big_grids = (rules[s] for s in small_grids)
    return merge(big_grids, (size // small_grid_size) * (small_grid_size + 1))


def main():
    with open("rules.txt") as f:
        rules = {}
        for line in f:
            old, new = map(str2tup, line.strip().split(" => "))
            for old_perm in gen_perms(old):
                rules[old_perm] = new

    grid = ((0, 1, 0), (0, 0, 1), (1, 1, 1))
    for i in range(18):
        grid = advance(grid, rules)
        if i in (4, 17):
            print(sum(sum(row) for row in grid))


if __name__ == "__main__":
    main()
