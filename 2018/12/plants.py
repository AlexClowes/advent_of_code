from collections import defaultdict
from itertools import count


def main():
    char2int = lambda c: ".#".find(c)
    with open("plants.txt") as f:
        plants = defaultdict(int, zip(count(), map(char2int, next(f).split()[-1])))
        next(f)
        rules = {}
        for line in f:
            pattern, result = line.split(" => ")
            rules[tuple(map(char2int, pattern))] = char2int(result)


def main():
    with open("plants.txt") as f:
        initial_state = next(f).split()[-1]
        plants = set(i for i, c in enumerate(initial_state) if c == "#")
        next(f)
        rules = {}
        for line in f:
            pattern, result = line.strip().split(" => ")
            rules[tuple(c == "#" for c in pattern)] = result == "#"

    def update(plants):
        new_plants = set()
        for i in range(min(plants) - 2, max(plants) + 3):
            pattern = tuple(j in plants for j in range(i - 2, i + 3))
            if rules[pattern]:
                new_plants.add(i)
        return new_plants

    for _ in range(20):
        plants = update(plants)
    print(sum(plants))

    # After a while, the sum increases linearly with the number of iterations
    for _ in range(80):
        plants = update(plants)
    sum100 = sum(plants)
    for _ in range(100):
        plants = update(plants)
    sum200 = sum(plants)
    n = 5 * 10 ** 10
    print((sum200 * (n - 100) + sum100 * (200 - n)) // 100)


if __name__ == "__main__":
    main()
