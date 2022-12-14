from itertools import pairwise


def get_range(lo, hi):
    return range(min(lo, hi), max(lo, hi) + 1)


def get_rocks(scan_line):
    for (x1, y1), (x2, y2) in pairwise(
        tuple(map(int, vertex.split(","))) for vertex in scan_line.split(" -> ")
    ):
        if x1 == x2:
            yield from ((x1, y) for y in get_range(y1, y2))
        else:
            yield from ((x, y1) for x in get_range(x1, x2))

        
def main():
    blocked = set()
    with open("rock_scan.txt") as f:
        for scan_line in f:
            for rock in get_rocks(scan_line):
                blocked.add(rock)

    floor = max(y for _, y in blocked) + 1

    def get_next_resting_place():
        x, y = 500, 0
        while y != floor:
            for dx in (0, -1, 1):
                if (x + dx, y + 1) not in blocked:
                    x, y = x + dx, y + 1
                    break
            else:
                break
        return x, y

    count = 0
    while (resting_place := get_next_resting_place()) != (500, 0):
        blocked.add(resting_place)
        count += 1
    count += 1

    print(count)


if __name__ == "__main__":
    main()
