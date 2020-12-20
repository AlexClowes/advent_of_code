from itertools import chain, product
import re

import numpy as np


TILE_DIMS = (10, 10)


class Tile:
    def __init__(self, id, data):
        self.id = id
        self.top = data[0]
        self.bottom = data[-1]
        self.left = data[:, 0]
        self.right = data[:, -1]

    def rotate(self):
        # Rotate 90 degrees anticlockwise
        old_top = self.top
        self.top = self.right
        self.right = self.bottom[::-1]
        self.bottom = self.left
        self.left = old_top[::-1]

    def flip(self):
        self.top, self.bottom = self.bottom, self.top
        self.left = self.left[::-1]
        self.right = self.right[::-1]


def permutations(tile):
    for _ in range(2):
        for __ in range(4):
            yield tile
            tile.rotate()
        tile.flip()


def adj(i, j):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1


def build_image(tiles):
    # Start by choosing an arbitrary tile and placing it at position (0, 0)
    image = {(0, 0): tiles.pop()}

    def fits(tile, i, j):
        return (
            ((i - 1, j) not in image or all(tile.top == image[i - 1, j].bottom))
            and ((i + 1, j) not in image or all(tile.bottom == image[i + 1, j].top))
            and ((i, j - 1) not in image or all(tile.left == image[i, j - 1].right))
            and ((i, j + 1) not in image or all(tile.right == image[i, j + 1].left))
        )

    # Keep going until every tile has been placed somewhere in the image
    while tiles:
        possible_positions = set(chain.from_iterable(adj(*p) for p in image))
        for tile, pos in product(tiles, possible_positions):
            if any(fits(permuted_tile, *pos) for permuted_tile in permutations(tile)):
                image[pos] = tile
                tiles.remove(tile)
                break
    return image


def corner_prod(image):
    imin = jmin = float("inf")
    imax = jmax = float("-inf")
    for i, j in image:
        imin = min(i, imin)
        imax = max(i, imax)
        jmin = min(j, jmin)
        jmax = max(j, jmax)
    return (
        image[imin, jmin].id
        * image[imin, jmax].id
        * image[imax, jmin].id
        * image[imax, jmax].id
    )


def main():
    tiles = set()
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
            tiles.add(Tile(tile_id, data))

    print(corner_prod(build_image(tiles)))


if __name__ == "__main__":
    main()
