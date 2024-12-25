import numpy as np


def main():
    with open("schematics.txt") as f:
        schematics = [
            np.array([list(line.strip()) for line in schematic.split("\n")]) == "#"
            for schematic in f.read().strip().split("\n\n")
        ]
    keys, locks = [], []
    for schematic in schematics:
        if schematic[0].all():
            keys.append(schematic)
        else:
            locks.append(schematic)
    print(sum(not (key & lock).any() for key in keys for lock in locks))


if __name__ == "__main__":
    main()
