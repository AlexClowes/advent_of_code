from collections import defaultdict
import numpy as np


def asteroids_by_dir(asteroid_map, point):
    visible = defaultdict(list)
    for i in range(asteroid_map.shape[0]):
        for j in range(asteroid_map.shape[0]):
            if asteroid_map[i, j] and (i, j) != point:
                visible[np.arctan2(j - point[1], i - point[0])].append((i, j))
    for angle in visible:
        magnitude = lambda pos: (point[0] - pos[0]) ** 2 + (point[1] - pos[1]) ** 2
        visible[angle] = sorted(visible[angle], key=magnitude)
    return visible


def main():
    with open("asteroids.txt") as f:
        asteroid_map = np.array([list(line.strip()) for line in f])
    asteroid_map = (asteroid_map == "#")

    best_count = 0
    for i in range(asteroid_map.shape[0]):
        for j in range(asteroid_map.shape[1]):
            if asteroid_map[i, j]:
                count = len(asteroids_by_dir(asteroid_map, (i, j)))
                if best_count < count:
                    best_count = count
                    best_point = i, j

    asteroids = asteroids_by_dir(asteroid_map, best_point)
    angles = sorted(asteroids.keys(), reverse=True)
    winner = asteroids[angles[199]][0]
    print(winner[1] * 100 + winner[0])


if __name__ == "__main__":
    main()
