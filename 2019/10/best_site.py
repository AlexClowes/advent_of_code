from fractions import Fraction

import numpy as np


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def visible_asteroids(asteroid_map, point):
    visible = set()
    for i in range(asteroid_map.shape[0]):
        for j in range(asteroid_map.shape[1]):
            if asteroid_map[i, j] and (i, j) != point:
                rel_pos = (i - point[0], j - point[1])
                sign = tuple(map(sgn, rel_pos))
                grad = Fraction(*rel_pos) if rel_pos[1] != 0 else float("inf")
                visible.add((sign, grad))
    return len(visible)


def main():
    with open("asteroids.txt") as f:
        asteroid_map = np.array([list(line.strip()) for line in f])
    asteroid_map = (asteroid_map == "#")

    asteroid_count = np.zeros_like(asteroid_map, dtype=np.int32)
    for i in range(asteroid_map.shape[0]):
        for j in range(asteroid_map.shape[1]):
            if asteroid_map[i, j]:
                asteroid_count[i, j] = visible_asteroids(asteroid_map, (i, j))
    print(np.max(asteroid_count))


if __name__ == "__main__":
    main()
