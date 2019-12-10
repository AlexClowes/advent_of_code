import numpy as np


def visible_asteroids(asteroid_map, point):
    visible = set()
    for i in range(asteroid_map.shape[0]):
        for j in range(asteroid_map.shape[1]):
            if asteroid_map[i, j] and (i, j) != point:
                visible.add(np.arctan2(i - point[0], j - point[1]))
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
