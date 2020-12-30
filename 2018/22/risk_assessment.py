from functools import lru_cache


def main():
    depth = 9465
    target = (13, 704)

    def geologic_index(x, y):
        if (x, y) == target:
            return 0
        if x == 0:
            return 48271 * y
        if y == 0:
            return 16807 * x
        return (erosion_level(x - 1, y) * erosion_level(x, y - 1)) % 20183

    @lru_cache(maxsize=None)
    def erosion_level(x, y):
        return (geologic_index(x, y) + depth) % 20183

    print(
        sum(
            erosion_level(x, y) % 3
            for x in range(target[0] + 1)
            for y in range(target[1] + 1)
        )
    )


if __name__ == "__main__":
    main()
