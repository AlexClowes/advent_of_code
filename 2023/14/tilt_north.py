def tilt_north(grid):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "O":
                i_rock = i
                while i_rock > 0 and grid[i_rock - 1][j] == ".":
                    i_rock -= 1
                grid[i][j] = "."
                grid[i_rock][j] = "O"


def load(grid):
    load = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "O":
                load += len(grid) - i
    return load


def main():
    with open("rocks.txt") as f:
        grid = [list(line.strip()) for line in f]

    tilt_north(grid)
    print(load(grid))


if __name__ == "__main__":
    main()
