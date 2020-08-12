from collections import namedtuple
from itertools import permutations
import re


Node = namedtuple("Node", "x y used avail")


def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def main():
    pat = r"/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T"
    with open("df.txt") as f:
        matches = (re.match(pat, line) for line in f)
        nodes = [Node(*map(try_int, m.groups())) for m in matches if m]

    print(sum(0 < na.used <= nb.avail for na, nb in permutations(nodes, 2)))


if __name__ == "__main__":
    main()
