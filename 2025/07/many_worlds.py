from collections import deque
from functools import cache


def main():
    with open("grid.txt") as f:
        grid = [line.strip() for line in f]
    height, width = len(grid), len(grid[0])

    @cache
    def propagate(i, j):
        if i == height:
            return 0
        if grid[i][j] == "^":
            return 1 + propagate(i, j - 1) + propagate(i, j + 1)
        return propagate(i + 1, j)

    start = next(j for j, char in enumerate(grid[0]) if char == "S")
    print(1 + propagate(0, start))


if __name__ == "__main__":
    main()
