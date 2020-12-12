import re

import numpy as np
import numba


EMPTY = 0
CLAY = 1
FLOWING_WATER = 2
STILL_WATER = 3


def print_state(state):
    print("\n".join("".join(".#|~"[x] for x in row) for row in state))
    print()


@numba.njit
def update(state):
    # Try to expand flowing water
    for i in range(state.shape[0] - 1):
        for j in range(state.shape[1]):
            if state[i, j] == FLOWING_WATER:
                # Try to go down
                if state[i + 1, j] == EMPTY:
                    state[i + 1, j] = FLOWING_WATER

                # Try to go left / right
                if state[i + 1, j] in (CLAY, STILL_WATER):
                    if state[i, j - 1] == EMPTY:
                        state[i, j - 1] = FLOWING_WATER
                    if state[i, j + 1] == EMPTY:
                        state[i, j + 1] = FLOWING_WATER

    # Any trapped flowing water becomes still water
    for i in range(state.shape[0] - 2, -1, -1):
        clay = [j for j in range(state.shape[1]) if state[i, j] == CLAY]
        for j0, j1 in zip(clay[:-1], clay[1:]):
            bounded = state[i, j0 + 1 : j1]
            support = state[i + 1, j0 + 1 : j1]
            if np.all(bounded == FLOWING_WATER) and np.all((support == CLAY) | (support == STILL_WATER)):
                state[i, j0 + 1 : j1] = STILL_WATER


def main():
    clay = set()
    pat = r"(x|y)=(\d+), (?:x|y)=(\d+)..(\d+)"
    with open("geology.txt") as f:
        for line in f:
            fixed_axis, fixed_coord, min_pos, max_pos = re.match(pat, line).groups()
            if fixed_axis == "x":
                x = int(fixed_coord)
                for y in range(int(min_pos), int(max_pos) + 1):
                    clay.add((x, y))
            else:
                y = int(fixed_coord)
                for x in range(int(min_pos), int(max_pos) + 1):
                    clay.add((x, y))

    xmin = min(x for (x, y) in clay)
    xmax = max(x for (x, y) in clay)
    ymin = min(y for (x, y) in clay)
    ymax = max(y for (x, y) in clay)

    state = np.zeros((ymax - ymin + 1, xmax - xmin + 3), dtype=int)
    for x, y in clay:
        state[y - ymin, x - xmin + 1] = CLAY

    state[0, 500 - xmin + 1] = FLOWING_WATER

    old_water_count = -1
    while True:
        update(state)
        water_count = np.sum((state == FLOWING_WATER) | (state == STILL_WATER))
        if old_water_count == water_count:
            break
        old_water_count = water_count

    print(water_count)
    print(np.sum(state == STILL_WATER))


if __name__ == "__main__":
    main()
