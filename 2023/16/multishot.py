from functools import cache


@cache
def interact(di, dj, element):
    if element == "/":
        return [(-dj, -di)]
    elif element == "\\":
        return [(dj, di)]
    elif element == "|" and dj != 0:
        return [(-1, 0), (1, 0)]
    elif element == "-" and di != 0:
        return [(0, -1), (0, 1)]
    else:
        return [(di, dj)]


def energised_count(grid, start_beam):
    grid = [row[:] for row in grid]
    i_max = len(grid)
    j_max = len(grid[0])
    energised = [[False for _ in range(j_max)] for _ in range(i_max)]

    seen = set()
    beams = [start_beam]
    while beams:
        i, j, di, dj = beams.pop()
        seen.add((i, j, di, dj))
        energised[i][j] = True
        for new_di, new_dj in interact(di, dj, grid[i][j]):
            new_i, new_j = i + new_di, j + new_dj
            if (
                0 <= new_i < i_max
                and 0 <= new_j < j_max
                and (new_i, new_j, new_di, new_dj) not in seen
            ):
                beams.append((new_i, new_j, new_di, new_dj))

    return sum(sum(row) for row in energised)


def main():
    with open("contraption.txt") as f:
        grid = [list(line.strip()) for line in f]

    i_max = len(grid)
    j_max = len(grid[0])
    max_energised = 0
    for i in range(i_max):
        max_energised = max(max_energised, energised_count(grid, (i, 0, 0, 1)))
        max_energised = max(max_energised, energised_count(grid, (i, j_max - 1, 0, -1)))
    for j in range(j_max):
        max_energised = max(max_energised, energised_count(grid, (0, j, 1, 0)))
        max_energised = max(max_energised, energised_count(grid, (i_max - 1, j, -1, 0)))
    print(max_energised)


if __name__ == "__main__":
    main()
