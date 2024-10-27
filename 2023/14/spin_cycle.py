def iter_rocks(grid, reverse_i=False, reverse_j=False):
    reverse_enumerate = lambda iterable: reversed(list(enumerate(iterable)))
    for i, row in (reverse_enumerate if reverse_i else enumerate)(grid):
        for j, char in (reverse_enumerate if reverse_j else enumerate)(row):
            if char == "O":
                yield i, j


def spin(grid):
    i_max = len(grid)
    j_max = len(grid[0])

    def tilt(di, dj, reverse_i=False, reverse_j=False):
        for i, j in iter_rocks(grid, reverse_i=reverse_i, reverse_j=reverse_j):
            i_rock, j_rock = i, j
            while (
                0 <= i_rock + di < i_max
                and 0 <= j_rock + dj < j_max
                and grid[i_rock + di][j_rock + dj] == "."
            ):
                i_rock += di
                j_rock += dj
            grid[i][j] = "."
            grid[i_rock][j_rock] = "O"

    tilt(-1, 0)
    tilt(0, -1)
    tilt(1, 0, reverse_i=True)
    tilt(0, 1, reverse_j=True)


def load(grid):
    load = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "O":
                load += len(grid) - i
    return load


def to_str(grid):
    return "\n".join("".join(row) for row in grid)


def to_grid(grid_str):
    return [list(row) for row in grid_str.split("\n")]


def main():
    with open("rocks.txt") as f:
        grid = [list(line.strip()) for line in f]

    past_states = []
    while (grid_str := to_str(grid)) not in past_states:
        past_states.append(grid_str)
        spin(grid)

    cycle_start = past_states.index(grid_str)
    cycle_len = len(past_states) - cycle_start

    N = 10**9
    grid = to_grid(past_states[N - ((N - cycle_start) // cycle_len) * cycle_len])
    print(load(grid))



if __name__ == "__main__":
    main()
