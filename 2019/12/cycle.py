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


def main():
    pat = r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)"
    with open("scan.txt") as f:
        scan = (re.match(pat, line).groups() for line in f)
        positions = np.fromiter(chain.from_iterable(scan), dtype=np.int32).reshape(-1, 3)
    velocities = np.zeros_like(positions)

    start_pos = np.copy(positions)
    start_vel = np.copy(velocities)

    count = 0
    first_repeat = np.zeros(3, dtype=np.int64)
    while True:
        count += 1
        step_forward(positions, velocities)
        for i in range(3):
            if (
                not first_repeat[i]
                and np.all(positions[:, i] == start_pos[:, i])
                and np.all(velocities[:, i] == start_vel[:, i])
            ):
                first_repeat[i] = count
        if np.all(first_repeat):
            break
    print(np.lcm.reduce(first_repeat))


if __name__ == "__main__":
    main()
