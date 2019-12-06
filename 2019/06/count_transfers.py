from collections import defaultdict
import re


def get_parent_chain(child, parents):
    parent_chain = [child]
    while child != "COM":
        child = parents[child]
        parent_chain.append(child)
    return parent_chain


def min_transfers(orbits, start, end):
    parents = {}
    for parent, child in orbits:
        parents[child] = parent
    start_parent_chain = get_parent_chain(start, parents)
    end_parent_chain = get_parent_chain(end, parents)
    for i, par1 in enumerate(start_parent_chain):
        for j, par2 in enumerate(end_parent_chain):
            if par1 == par2:
                return i + j


def main():
    with open("orbits.txt") as f:
        orbits = (re.match(r"(\w+)\)(\w+)", line).groups() for line in f)
        print(min_transfers(orbits, "YOU", "SAN") - 2)


if __name__ == "__main__":
    main()
