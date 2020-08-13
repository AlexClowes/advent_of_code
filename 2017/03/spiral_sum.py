from collections import defaultdict
from itertools import count


def spiral_positions():
    x, y = 0, 0
    for n in count(1):
        delta = 2 * (n % 2) - 1
        for _ in range(n):
            x += delta
            yield x, y
        for _ in range(n):
            y += delta
            yield x, y


def adj(x, y):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            yield x + dx, y + dy


def main():
    data = defaultdict(int)
    data[0, 0] = 1
    for (x, y) in spiral_positions():
        s = sum(data[a] for a in adj(x, y))
        if s > 289326:
            print(s)
            return
        data[x, y] = s


if __name__ == "__main__":
    main()
