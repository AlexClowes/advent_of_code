def adj(x, y, z):
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)


def main():
    with open("cubes.txt") as f:
        cubes = set(tuple(map(int, line.strip().split(","))) for line in f)

    print(sum(adj_cube not in cubes for cube in cubes for adj_cube in adj(*cube)))


if __name__ == "__main__":
    main()
