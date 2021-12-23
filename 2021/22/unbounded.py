from math import prod
import re


class Block:
    def __init__(self, bounds, value):
        self.bounds = bounds
        self.value = value

    def __and__(self, other):
        bounds = []
        for (lower1, upper1), (lower2, upper2) in zip(self.bounds, other.bounds):
            lower = max(lower1, lower2)
            upper = min(upper1, upper2)
            if lower >= upper:
                return None
            bounds.append((lower, upper))
        return Block(bounds, -other.value)

    def size(self):
        return self.value * prod(upper - lower for lower, upper in self.bounds)


def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def main():
    blocks = []
    with open("instructions.txt") as f:
        for i, line in enumerate(f):
            state, xmin, xmax, ymin, ymax, zmin, zmax = map(
                try_int,
                re.match(
                    r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)",
                    line,
                ).groups()
            )
            new_block = Block(
                ((xmin, xmax + 1), (ymin, ymax + 1), (zmin, zmax + 1)), state=="on"
            )
            blocks += list(filter(None, (new_block & old_block for old_block in blocks)))
            if new_block.value:
                blocks.append(new_block)
        print(sum(block.size() for block in blocks))


if __name__ == "__main__":
    main()
