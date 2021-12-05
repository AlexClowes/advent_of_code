from collections import defaultdict
import re


def parse_line(line_str):
    pattern = r"(\d+),(\d+) -> (\d+),(\d+)"
    x1, y1, x2, y2 = map(int, re.match(pattern, line_str).groups())
    return x1, y1, x2, y2


def coord_iter(start, end):
    if start == end:
        while True:
            yield start
    direction = 1 if start < end else -1
    yield from range(start, end + direction, direction)


def build_map(lines):
    vent_map = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        if x1 != x2 and y1 != y2:
            continue
        for coord in zip(coord_iter(x1, x2), coord_iter(y1, y2)):
            vent_map[coord] += 1
    return vent_map


def main():
    with open("lines.txt") as f:
        lines = [parse_line(line) for line in f]

    print(sum(count > 1 for count in build_map(lines).values()))


if __name__ == "__main__":
    main()
