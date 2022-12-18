from collections import deque
from itertools import product


def adj(x, y, z):
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)


def main():
    with open("cubes.txt") as f:
        lava_cubes = set(tuple(map(int, line.strip().split(","))) for line in f)

    # Get bounding box
    bounds = [
        (min(c[i] for c in lava_cubes) - 1, max(c[i] for c in lava_cubes) + 1)
        for i in range(3)
    ]
    # Find a single non-lava cube in the box
    start = next(
        cube
        for cube in product(*(range(lo, hi) for lo, hi in bounds))
        if cube not in lava_cubes
    )
    # Flood fill to find all exterior cubes
    q = deque([start])
    ext_cubes = set()
    while q:
        cube = q.popleft()
        if (
            cube in ext_cubes
            or cube in lava_cubes
            or not all(lo <= v <= hi for v, (lo, hi) in zip(cube, bounds))
        ):
            continue
        ext_cubes.add(cube)
        q.extend(adj(*cube))

    print(sum(adj_cube in ext_cubes for cube in lava_cubes for adj_cube in adj(*cube)))


if __name__ == "__main__":
    main()
