from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __gt__(self, other):
        return (self.value - other.value) % 3 == 1


def score(their_move, my_move):
    ret = my_move.value
    if my_move > their_move:
        return ret + 6
    if my_move is their_move:
        return ret + 3
    return ret


def main():
    move_lookup = {
        "A": Move.ROCK,
        "B": Move.PAPER,
        "C": Move.SCISSORS,
        "X": Move.ROCK,
        "Y": Move.PAPER,
        "Z": Move.SCISSORS,
    }
    with open("cheatsheet.txt") as f:
        moves = (tuple(map(move_lookup.get, line.split())) for line in f)
        print(sum(score(m1, m2) for m1, m2 in moves))


if __name__ == "__main__":
    main()
