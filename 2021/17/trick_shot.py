import re


def main():
    with open("region.txt") as f:
        pat = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"
        xmin, xmax, ymin, ymax = map(int, re.match(pat, f.read().strip()).groups())

    def gen_y(v0):
        y = 0
        yield y
        while y >= ymin:
            y += v0
            v0 -= 1
            yield y

    v0_t_pairs = {
        v0: set(t for t, y in enumerate(gen_y(v0)) if ymin <= y <= ymax)
        for v0 in range(ymin, -ymin + 1)
    }

    # Part 1
    print(max(v0 * (v0 - 1) // 2 for v0 in v0_t_pairs if v0 > 0))

    def x(u0, t):
        if t < u0:
            return u0 * t - t * (t - 1) // 2
        return u0 * (u0 + 1) // 2

    # Part 2
    print(
        sum(
            any(xmin <= x(u0, t) <= xmax for t in t_vals)
            for u0 in range(xmax + 1)
            for v0, t_vals in v0_t_pairs.items()
        )
    )


if __name__ == "__main__":
    main()
