from collections import defaultdict
import re


def build_tree(orbits):
    tree = defaultdict(list)
    for parent, child in orbits:
        tree[parent].append(child)
    return tree


def count_orbits(orbits):
    tree = build_tree(orbits)
    orbits = {}
    def recurse(body, val):
        orbits[body] = val
        for child in tree[body]:
            recurse(child, val + 1)
    recurse("COM", 0)
    return sum(orbits.values())


def main():
    with open("orbits.txt") as f:
        orbits = (re.match(r"(\w+)\)(\w+)", line).groups() for line in f)
        print(count_orbits(orbits))


if __name__ == "__main__":
    main()
