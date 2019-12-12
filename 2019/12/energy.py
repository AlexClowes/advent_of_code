from itertools import chain
import re

import numpy as np


def step_forward(positions, velocities):
    for i in range(positions.shape[0]):
        for j in range(i + 1, positions.shape[0]):
            pos_diff = np.sign(positions[i] - positions[j])
            velocities[i] -= pos_diff
            velocities[j] += pos_diff
    positions += velocities


def energy(positions, velocities):
    ke = np.sum(np.abs(positions), axis=1)
    pe = np.sum(np.abs(velocities), axis=1)
    return np.sum(ke * pe)


def main():
    pat = r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)"
    with open("scan.txt") as f:
        scan = (re.match(pat, line).groups() for line in f)
        positions = np.fromiter(chain.from_iterable(scan), dtype=np.int32).reshape(-1, 3)
    velocities = np.zeros_like(positions)

    for _ in range(1000):
        step_forward(positions, velocities)

    print(energy(positions, velocities))


if __name__ == "__main__":
    main()
