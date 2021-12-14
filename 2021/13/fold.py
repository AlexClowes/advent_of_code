def display(dots):
    xmin = min(x for x, _ in dots)
    xmax = max(x for x, _ in dots)
    ymin = min(y for _, y in dots)
    ymax = max(y for _, y in dots)
    print(
        "\n".join(
            "".join(" #"[(x, y) in dots] for x in range(xmin, xmax + 1))
            for y in range(ymin, ymax + 1)
        )
    )


def fold(dots, direction, pos):
    if direction == "x":
        def move(x, y):
            return x if x < pos else 2 * pos - x, y
    else:
        def move(x, y):
            return x, y if y < pos else 2 * pos - y
    return {move(x, y) for x, y in dots}


def main():
    with open("transparency.txt") as f:
        dots = set()
        for line in f:
            if line == "\n":
                break
            dots.add(tuple(map(int, line.strip().split(","))))
        for i, line in enumerate(f):
            direction, val = line.strip().split()[-1].split("=")
            dots = fold(dots, direction, int(val))
            if i == 0:
                print(len(dots))  # Part 1
    display(dots)


if __name__ == "__main__":
    main()
