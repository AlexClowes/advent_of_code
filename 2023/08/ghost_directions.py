from collections import defaultdict
from itertools import cycle
from math import lcm
import re


def main():
    with open("map.txt") as f:
        instructions = f.readline().strip()
        f.readline()
        network = defaultdict(dict)
        for line in f:
            start, left_dest, right_dest = re.match("(\w+) = \((\w+), (\w+)\)", line).groups()
            network[start]["L"] = left_dest
            network[start]["R"] = right_dest

    def count_the_steps(pos):
        steps = 0
        for direction in cycle(instructions):
            steps += 1
            pos = network[pos][direction]
            if pos.endswith("Z"):
                return steps
    
    print(lcm(*(count_the_steps(pos) for pos in network if pos.endswith("A"))))


if __name__ == "__main__":
    main()
