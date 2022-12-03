from enum import Enum


class Move(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    @property
    def score(self):
        return self.value + 1

    @property
    def beats(self):
        return Move((self.value - 1) % 3)

    @property
    def beaten_by(self):
        return Move((self.value + 1) % 3)


class Result(Enum):
    LOSE = 0
    DRAW = 1
    WIN = 2

    @property
    def score(self):
        return self.value * 3


def score(their_move, result):
    ret = result.score
    if result is Result.LOSE:
        return ret + their_move.beats.score
    elif result is Result.DRAW:
        return ret + their_move.score
    else:
        return ret + their_move.beaten_by.score


def main():
    lookup = {
        "A": Move.ROCK,
        "B": Move.PAPER,
        "C": Move.SCISSORS,
        "X": Result.LOSE,
        "Y": Result.DRAW,
        "Z": Result.WIN,
    }
    with open("cheatsheet.txt") as f:
        moves = (tuple(map(lookup.get, line.split())) for line in f)
        print(sum(score(m1, m2) for m1, m2 in moves))


if __name__ == "__main__":
    main()
