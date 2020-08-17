directions = {
    "n": (0, 1),
    "ne": (0.5, 0.5),
    "se": (0.5, -0.5),
    "s": (0, -1),
    "sw": (-0.5, -0.5),
    "nw": (-0.5, 0.5),
}


def main():
    x, y = 0, 0
    max_dist = 0
    with open("path.txt") as f:
        for d in f.read().strip().split(","):
            dx, dy = directions[d]
            x, y = x + dx, y + dy
            max_dist = max(max_dist, abs(x) + abs(y))
    print(int(abs(x) + abs(y)))
    print(int(max_dist))


if __name__ == "__main__":
    main()
