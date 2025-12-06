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

    total = sum(
        rolls[i][j] == "@" and sum(rolls[ai][aj] == "@" for ai, aj in adj(i, j)) < 4
        for i in range(1, height + 1)
        for j in range(1, width + 1)
    )
    print(total)


if __name__ == "__main__":
    main()
