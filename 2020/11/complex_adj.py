def los_occupied(y, x, dy, dx, occupied, xmax, ymax):
    while 0 <= x <= xmax and 0 <= y <= ymax:
        x += dx
        y += dy
        if (y, x) in occupied:
            return occupied[y, x]
    return False


def count_los(pos, occupied, xmax, ymax):
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    return sum(los_occupied(*pos, *d, occupied, xmax, ymax) for d in directions)


def iterate(occupied, xmax, ymax):
    new_occupied = {}
    changed = False
    for pos, occ in occupied.items():
        count = count_los(pos, occupied, xmax, ymax)
        if occ:
            new_occupied[pos] = count < 5
        else:
            new_occupied[pos] = count == 0
        if occupied[pos] != new_occupied[pos]:
            changed = True
    return new_occupied, changed


def main():
    occupied = {}
    with open("layout.txt") as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line.strip()):
                if char == "L":
                    occupied[i, j] = False
    ymax, xmax = i, j

    changed = True
    while changed:
        occupied, changed = iterate(occupied, xmax, ymax)
    print(sum(occupied.values()))


if __name__ == "__main__":
    main()
