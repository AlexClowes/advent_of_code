from collections import defaultdict


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

    inf_points = set()
    areas = defaultdict(int)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            min_dist = 99999
            for point in points:
                dist = manhattan_metric(point, (x, y))
                if dist < min_dist:
                    tie = False
                    min_dist = dist
                    closest_point = point
                elif dist == min_dist:
                    tie = True
            if not tie:
                areas[closest_point] += 1
                if x in (min_x, max_x) or y in (min_y, max_y):
                    inf_points.add(closest_point)

    print(max(area for point, area in areas.items() if point not in inf_points))


if __name__ == "__main__":
    main()
