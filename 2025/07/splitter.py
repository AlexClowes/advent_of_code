from collections import deque


def main():
    with open("grid.txt") as f:
        grid = [line.strip() for line in f]
    height, width = len(grid), len(grid[0])

    seen = set()

    def propagate(i, j):
        if (i, j) in seen:
            return 0
        seen.add((i, j))
        if i == height:
            return 0
        if grid[i][j] == "^":
            return 1 + propagate(i, j - 1) + propagate(i, j + 1)
        return propagate(i + 1, j)

    start = next(j for j, char in enumerate(grid[0]) if char == "S")
    print(propagate(0, start))


if __name__ == "__main__":
    main()
