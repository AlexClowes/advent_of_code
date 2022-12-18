from collections import namedtuple
from itertools import chain, cycle

import numpy as np


class Block(namedtuple("Block", ("x", "y"))):
    def move(self, dx, dy):
        return Block(self.x + dx, self.y + dy)


SHAPES = [
    [Block(0, 0), Block(1, 0), Block(2, 0), Block(3, 0)],
    [Block(1, 0), Block(0, 1), Block(1, 1), Block(2, 1), Block(1, 2)],
    [Block(0, 0), Block(1, 0), Block(2, 0), Block(2, 1), Block(2, 2)],
    [Block(0, 0), Block(0, 1), Block(0, 2), Block(0, 3)],
    [Block(0, 0), Block(1, 0), Block(0, 1), Block(1, 1)],
]


class Tetris:
    def __init__(self):
        self.shapes = cycle(SHAPES)
        self.columns = [{0} for _ in range(7)]
        self.colmax = [0] * 7
        self.blocks = None

    @property
    def tower_height(self):
        return max(self.colmax)

    def spawn(self):
        self.blocks = next(self.shapes)
        assert self.move_blocks(2, 4 + self.tower_height)

    def freeze_blocks(self):
        for block in self.blocks:
            self.columns[block.x].add(block.y)
            self.colmax[block.x] = max(self.colmax[block.x], block.y)
        self.blocks = None

    def move_blocks(self, dx, dy):
        new_blocks = [block.move(dx, dy) for block in self.blocks]
        if legal_move := all(
            0 <= block.x < 7 and block.y not in self.columns[block.x]
            for block in new_blocks
        ):
            self.blocks = new_blocks
        return legal_move


def get_tower_heights(winds, turns):
    yield 0
    winds = cycle(winds)
    game = Tetris()
    for _ in range(turns):
        game.spawn()
        while True:
            game.move_blocks(next(winds), 0)
            if not (moved_down := game.move_blocks(0, -1)):
                break
        game.freeze_blocks()
        yield game.tower_height


def main():
    with open("winds.txt") as f:
        winds = [{"<": -1, ">": 1}[c] for c in f.read().strip()]

    # Assume ∃ T, n, m s.t. ∀ t > T h(t + n) = h(t) + m
    # Then for x > T, say x = T + kn + r, and then
    # h(x) = h(T + r + kn) = h(T + r) + km

    # Find candidates for T, n, m
    search_size = 5000
    heights = np.array(list(get_tower_heights(winds, search_size)))
    for n in range(1, search_size // 2):
        diff = heights.copy()
        diff[n:] -= heights[:-n]
        if (diff[search_size // 2:] == diff[-1]).all():
            break
    T = search_size // 2
    m = diff[-1]

    x = 10 ** 12
    k, r = divmod(x - T, n)
    print(heights[T + r] + k * m)


if __name__ == "__main__":
    main()
