def interact(di, dj, element):
    if element == "/":
        yield -dj, -di
    elif element == "\\":
        yield dj, di
    elif element == "|" and dj != 0:
        yield (-1, 0)
        yield (1, 0)
    elif element == "-" and di != 0:
        yield (0, -1)
        yield (0, 1)
    else:
        yield di, dj


def main():
    with open("contraption.txt") as f:
        grid = [list(line.strip()) for line in f]
    i_max = len(grid)
    j_max = len(grid[0])
    energised = [[False for _ in range(j_max)] for _ in range(i_max)]

    seen = set()
    beams = [(0, 0, 0, 1)]
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

    print(sum(energised[i][j] for i in range(i_max) for j in range(j_max)))


if __name__ == "__main__":
    main()
