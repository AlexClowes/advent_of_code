from itertools import count
import re


def first_time(n_positions, start_position):
    for t in count():
        if all(
            (s + t + i) % n == 0
            for i, (n, s) in enumerate(zip(n_positions, start_position), 1)
        ):
            return t


def main():
    n_positions = []
    start_position = []
    with open("discs.txt") as f:
        for line in f:
            pat = r"Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+)."
            n, s = map(int, re.match(pat, line.strip()).groups())
            n_positions.append(n)
            start_position.append(s)

    print(first_time(n_positions, start_position))

    n_positions.append(11)
    start_position.append(0)
    print(first_time(n_positions, start_position))


if __name__ == "__main__":
    main()
