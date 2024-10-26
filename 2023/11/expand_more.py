from itertools import combinations


def transpose(grid):
    return list(zip(*grid))


def empty_rows_indices(grid):
    return [i for i, row in enumerate(grid) if all(char == "." for char in row)]


def main():
    with open("image.txt") as f:
        grid = [list(line.strip()) for line in f]

    scale_factor = 10 ** 6
    empty_rows = empty_rows_indices(grid)
    empty_cols = empty_rows_indices(transpose(grid))

    def distance(pos1, pos2):
        dist = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
        for empty_row in empty_rows:
            if min(pos1[0], pos2[0]) < empty_row < max(pos1[0], pos2[0]):
                dist += scale_factor - 1
        for empty_col in empty_cols:
            if min(pos1[1], pos2[1]) < empty_col < max(pos1[1], pos2[1]):
                dist += scale_factor - 1
        return dist

    galaxy_coords = (
        (i, j)
        for i, row in enumerate(grid)
        for j, char in enumerate(row)
        if char == "#"
    )
    distances = (distance(g1, g2) for g1, g2 in combinations(galaxy_coords, 2))
    print(sum(distances))


if __name__ == "__main__":
    main()
