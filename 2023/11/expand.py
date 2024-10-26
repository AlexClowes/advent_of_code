from itertools import combinations


def transpose(grid):
    return list(map(list, zip(*grid)))


def expand_rows(grid):
    def new_rows():
        for row in grid:
            if all(char == "." for char in row):
                yield row
            yield row

    return list(new_rows())


def expand(grid):
    return expand_rows(transpose(expand_rows(transpose(grid))))


def main():
    with open("image.txt") as f:
        grid = expand([list(line.strip()) for line in f])

    galaxy_coords = (
        (i, j)
        for i, row in enumerate(grid)
        for j, char in enumerate(row)
        if char == "#"
    )
    distances = [
        abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        for g1, g2 in combinations(galaxy_coords, 2)
    ]
    print(sum(distances))



if __name__ == "__main__":
    main()
