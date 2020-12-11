def adj(i, j):
    yield i - 1, j - 1
    yield i - 1, j
    yield i - 1, j + 1
    yield i, j - 1
    yield i, j + 1
    yield i + 1, j - 1
    yield i + 1, j
    yield i + 1, j + 1


def count_adj(pos, occupied):
    return sum(occupied.get(a, 0) for a in adj(*pos))


def iterate(occupied):
    new_occupied = {}
    changed = False
    for pos, occ in occupied.items():
        count = count_adj(pos, occupied)
        if occ:
            new_occupied[pos] = count < 4
        else:
            new_occupied[pos] = count == 0
        changed = changed or (occupied[pos] ^ new_occupied[pos])
    return new_occupied, changed


def main():
    occupied = {}
    with open("layout.txt") as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line.strip()):
                if char == "L":
                    occupied[i, j] = False

    changed = True
    while changed:
        occupied, changed = iterate(occupied)
    print(sum(occupied.values()))


if __name__ == "__main__":
    main()
