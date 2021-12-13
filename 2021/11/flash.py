import numpy as np


def main():
    with open("octopuses.txt") as f:
        octopuses = np.array([[int(char) for char in line.strip()] for line in f])

    def adj(i, j):
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if 0 <= i + di < octopuses.shape[0] and 0 <= j + dj < octopuses.shape[1]:
                    yield i + di, j + dj

    def iterate():
        nonlocal octopuses
        octopuses += 1
        flashed = set()
        to_check = set(np.ndindex(octopuses.shape))
        while to_check:
            pos = to_check.pop()
            if octopuses[pos] > 9 and pos not in flashed:
                flashed.add(pos)
                for new_pos in adj(*pos):
                    octopuses[new_pos] += 1
                    to_check.add(new_pos)
        for pos in flashed:
            octopuses[pos] = 0
        return len(flashed)

    print(sum(iterate() for _ in range(100)))


if __name__ == "__main__":
    main()
