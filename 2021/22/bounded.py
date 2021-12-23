from collections import defaultdict
from itertools import product
import re


def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def bound(a, b):
    bounds = -50, 50
    return range(max(a, bounds[0]), min(b, bounds[1]) + 1)


def main():
    cubes = defaultdict(int)
    with open("instructions.txt") as f:
        for line in f:
            state, xmin, xmax, ymin, ymax, zmin, zmax = map(
                try_int,
                re.match(
                    r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)",
                    line,
                ).groups()
            )
            for x, y, z in product(
                bound(xmin, xmax), bound(ymin, ymax), bound(zmin, zmax)
            ):
                cubes[x, y, z] = state == "on"
        print(sum(cubes.values()))


if __name__ == "__main__":
    main()
