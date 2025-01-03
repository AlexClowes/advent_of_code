from typing import NamedTuple


class Coord(NamedTuple):
    i: int
    j: int

    def __add__(self, other):
        return self.__class__(self.i + other.i, self.j + other.j)


NORTH = Coord(-1, 0)
SOUTH = Coord(1, 0)
EAST = Coord(0, 1)
WEST = Coord(0, -1)

CONNECTIONS = {
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    "L": (NORTH, EAST),
    "J": (NORTH, WEST),
    "7": (SOUTH, WEST),
    "F": (SOUTH, EAST),
    ".": (),
}


def main():
    with open("sketch.txt") as f:
        grid = [list(line.strip()) for line in f]

    for i_start, row in enumerate(grid):
        for j_start, char in enumerate(row):
            if char == "S":
                start_pos = Coord(i_start, j_start)
                break

    # Find pipes that connect directly to S, confirm there are exactly two
    possible_first_positions = []
    for move in (Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1)):
        candidate = start_pos + move
        if any(
            candidate + legal_move == start_pos
            for legal_move in CONNECTIONS[grid[candidate.i][candidate.j]]
        ):
                possible_first_positions.append(candidate)
    assert len(possible_first_positions) == 2

    # Aribtrarily start with one of the two connecting pipes
    last, curr = start_pos, possible_first_positions[0]
    loop_coords = [start_pos]
    while curr != start_pos:
        loop_coords.append(curr)
        moves = CONNECTIONS[grid[curr.i][curr.j]]
        last, curr = curr, next(curr + move for move in moves if curr + move != last)

    # Shoelace formula
    loop_coords.append(loop_coords[0])
    area = abs(
        sum(a.i * b.j - b.i * a.j for a, b in zip(loop_coords, loop_coords[1:]))
    ) // 2
    print(area - (len(loop_coords) - 1) // 2 + 1)


if __name__ == "__main__":
    main()
