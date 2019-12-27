def manhattan_metric(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def main():
    with open("points.txt") as f:
        points = {tuple(map(int, line.strip().split(","))) for line in f}

    min_x = 99999
    max_x = 0
    min_y = 99999
    max_y = 0
    for point in points:
        min_x = min(min_x, point[0])
        max_x = max(max_x, point[0])
        min_y = min(min_y, point[1])
        max_y = max(max_y, point[1])

    area = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if sum(manhattan_metric(point, (x, y)) for point in points) < 10000:
                area += 1
    print(area)


if __name__ == "__main__":
    main()
