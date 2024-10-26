from collections import defaultdict
from itertools import cycle
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

    pos = "AAA"
    steps = 0
    for direction in cycle(instructions):
        steps += 1
        pos = network[pos][direction]
        if pos == "ZZZ":
            break
    print(steps)



if __name__ == "__main__":
    main()
