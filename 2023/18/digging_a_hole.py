import re


HEADINGS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def parse_line(line):
    heading_str, distance, _ = re.match("(\w) (\d+) \(#([\d\w]+)\)", line).groups()
    return HEADINGS[heading_str], int(distance)


def main():
    # Dig trench
    with open("dig_plan.txt") as f:
        i = j = 0
        dug = {(i, j)}
        for line in f:
            (di, dj), dist = parse_line(line.strip())
            for _ in range(dist):
                i += di
                j += dj
                dug.add((i, j))

    # Find an interior point
    i_min = j_min = float("inf")
    i_max = j_max = float("-inf")
    for i, j in dug:
        i_min = min(i_min, i)
        i_max = max(i_max, i)
        j_min = min(j_min, j)
        j_max = max(j_max, j)

    found_interior = False
    for i in range(i_min + 1, i_max):
        touched_boundary = False
        for j in range(j_min, j_max):
            if not touched_boundary and (i, j) in dug:
                touched_boundary = True
            if touched_boundary and (i, j) not in dug:
                found_interior = True
                break
        if found_interior:
            break

    # Flood fill from interior point
    def adj(i, j):
        yield i + 1, j
        yield i - 1, j
        yield i, j + 1
        yield i, j - 1

    q = {(i, j)}
    while q:
        i, j = q.pop()
        dug.add((i, j))
        for i, j in adj(i, j):
            if (i, j) not in dug:
                q.add((i, j))

    print(len(dug))


if __name__ == "__main__":
    main()
