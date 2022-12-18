from collections import namedtuple
from itertools import chain, cycle


class Block(namedtuple("Block", ("x", "y"))):
    def move(self, dx, dy):
        return Block(self.x + dx, self.y + dy)


SHAPES = cycle(
    [
        [Block(0, 0), Block(1, 0), Block(2, 0), Block(3, 0)],
        [Block(1, 0), Block(0, 1), Block(1, 1), Block(2, 1), Block(1, 2)],
        [Block(0, 0), Block(1, 0), Block(2, 0), Block(2, 1), Block(2, 2)],
        [Block(0, 0), Block(0, 1), Block(0, 2), Block(0, 3)],
        [Block(0, 0), Block(1, 0), Block(0, 1), Block(1, 1)],
    ]
)


class Tetris:
    def __init__(self):
        self.columns = [{0} for _ in range(7)]
        self.blocks = None

    @property
    def tower_height(self):
        return max(chain(*self.columns))

    def freeze_blocks(self):
        for block in self.blocks:
            self.columns[block.x].add(block.y)
        self.blocks = None

    def move_blocks(self, dx, dy):
        new_blocks = [block.move(dx, dy) for block in self.blocks]
        if legal_move := all(
            0 <= block.x < 7 and block.y not in self.columns[block.x]
            for block in new_blocks
        ):
            self.blocks = new_blocks
        return legal_move

    def spawn(self):
        self.blocks = next(SHAPES)
        assert self.move_blocks(2, 4 + self.tower_height)


def main():
    with open("winds.txt") as f:
        winds = cycle({"<": -1, ">": 1}[c] for c in f.read().strip())

    game = Tetris()
    for _ in range(2022):
        game.spawn()
        while True:
            game.move_blocks(next(winds), 0)
            moved_down = game.move_blocks(0, -1)
            if not moved_down:
                game.freeze_blocks()
                break

    print(game.tower_height)


if __name__ == "__main__":
    main()
