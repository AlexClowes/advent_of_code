from collections import deque
import re

import numpy as np


TILE_DIMS = (10, 10)

TOP = 0
BOTTOM = -1
LEFT = (slice(None), 0)
RIGHT = (slice(None), -1)

MONSTER = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    ],
    dtype=bool,
)


def permute(arr):
    for _ in range(2):
        for _ in range(4):
            yield arr
            arr[:] = np.rot90(arr)
        arr[:] = arr[::-1]


def adj(i, j):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1


def get_bounds(grid):
    imin = jmin = float("inf")
    imax = jmax = float("-inf")
    for i, j in grid:
        imin = min(i, imin)
        imax = max(i, imax)
        jmin = min(j, jmin)
        jmax = max(j, jmax)
    return imin, imax + 1, jmin, jmax + 1


def build_image(tiles):
    # Start by choosing an arbitrary tile and placing it at position (0, 0)
    grid = {(0, 0): tiles.popitem()[1]}
    possible_positions = deque(adj(0, 0))

    def fits(tile, i, j):
        return (
            ((i - 1, j) not in grid or all(tile[TOP] == grid[i - 1, j][BOTTOM]))
            and ((i + 1, j) not in grid or all(tile[BOTTOM] == grid[i + 1, j][TOP]))
            and ((i, j - 1) not in grid or all(tile[LEFT] == grid[i, j - 1][RIGHT]))
            and ((i, j + 1) not in grid or all(tile[RIGHT] == grid[i, j + 1][LEFT]))
        )

    # Keep going until every tile has been placed somewhere in the grid
    while tiles and possible_positions:
        pos = possible_positions.popleft()
        for (tile_id, tile) in tiles.items():
            if any(fits(permuted_tile, *pos) for permuted_tile in permute(tile)):
                grid[pos] = tile
                tiles.pop(tile_id)
                possible_positions.extend(filter(lambda p: p not in grid, adj(*pos)))
                break

    # Build single large array from tiles
    imin, imax, jmin, jmax = get_bounds(grid)
    subtile_dims = (TILE_DIMS[0] - 2, TILE_DIMS[1] - 2)
    image_dims = (
        (imax - imin) * subtile_dims[0],
        (jmax - jmin) * subtile_dims[1],
    )
    image = np.zeros(image_dims, dtype=bool)
    for i in range(0, imax - imin):
        for j in range(0, jmax - jmin):
            image[
                i * subtile_dims[0] : (i + 1) * subtile_dims[0],
                j * subtile_dims[1] : (j + 1) * subtile_dims[1],
            ] = grid[i + imin, j + jmin][1:-1, 1:-1]

    return image


def hunt_monsters(image):
    count = 0
    for i in range(image.shape[0] - MONSTER.shape[0] + 1):
        for j in range(image.shape[1] - MONSTER.shape[1] + 1):
            image_slice = image[i : i + MONSTER.shape[0], j : j + MONSTER.shape[1]]
            if np.all(image_slice | ~MONSTER):
                count += 1
    return count


def main():
    tiles = {}
    with open("tiles.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            tile_id = int(re.match(r"Tile (\d+)", line).group(1))
            data = np.zeros(TILE_DIMS, dtype=bool)
            for i, line in enumerate(f):
                if line == "\n":
                    break
                for j, char in enumerate(line.strip()):
                    data[i, j] = char == "#"
            tiles[tile_id] = data

    image = build_image(tiles)
    for permuted_image in permute(image):
        if count := hunt_monsters(permuted_image):
            print(np.sum(image) - count * np.sum(MONSTER))


if __name__ == "__main__":
    main()
