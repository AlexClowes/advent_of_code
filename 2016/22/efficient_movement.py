from collections import namedtuple
from itertools import permutations
import re

import matplotlib.pyplot as plt


Node = namedtuple("Node", "x y used avail")


def main():
    pat = r"/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T"
    with open("df.txt") as f:
        matches = (re.match(pat, line) for line in f)
        nodes = [Node(*map(int, m.groups())) for m in matches if m]

    xyused = ((n.x, n.y, n.used) for n in nodes)
    plt.scatter(*zip(*xyused))
    plt.show()

    # After plotting, calculate by hand
    print(17 + 2 + 34 + 20 + 1 + 5 * 34)


if __name__ == "__main__":
    main()
