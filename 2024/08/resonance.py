from collections import defaultdict
from itertools import product
import numpy as np


def main():
    with open("antennae.txt") as f:
        arr = np.array([list(line.strip()) for line in f])
    bounds = arr.shape

    antenna_locs = defaultdict(list)
    for pos, char in np.ndenumerate(arr):
        if char.isalpha() or char.isdigit():
            antenna_locs[char].append(np.array(pos))

    antinodes = set()
    for frequency, positions in antenna_locs.items():
        for pos1, pos2 in product(positions, repeat=2):
            if pos1 is pos2:
                continue
            dpos = pos1 - pos2
            antinode = pos1.copy()
            while ((0 <= antinode) & (antinode < bounds)).all():
                antinodes.add(tuple(antinode))
                antinode += dpos

    print(len(antinodes))


if __name__ == "__main__":
    main()
