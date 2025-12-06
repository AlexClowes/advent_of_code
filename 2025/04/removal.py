from copy import deepcopy


def adj(i, j):
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di != 0 or dj != 0:
                yield i + di, j + dj


def main():
    with open("rolls.txt") as f:
        rolls = [["."] + list(line.strip()) + ["."] for line in f]
    height, width = len(rolls), len(rolls[0]) - 2
    rolls = [["."] * (width + 2)] + rolls + [["."] * (width + 2)]

    def remove():
        nonlocal rolls
        new_rolls = deepcopy(rolls)
        removed = 0
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                if (
                    rolls[i][j] == "@"
                    and sum(rolls[ai][aj] == "@" for ai, aj in adj(i, j)) < 4
                ):
                    new_rolls[i][j] = "."
                    removed += 1
        rolls = new_rolls
        return removed

    total = 0
    while removed := remove():
        total += removed
    print(total)


if __name__ == "__main__":
    main()
