HEADINGS = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (1 / 2, 1),
    "nw": (-1 / 2, 1),
    "se": (1 / 2, -1),
    "sw": (-1 / 2, -1),
}


def split_dirs(directions):
    pos = 0
    while pos < len(directions):
        if directions[pos] in "ns":
            yield directions[pos : pos + 2]
            pos += 2
        else:
            yield directions[pos]
            pos += 1


def get_pos(directions):
    x, y = 0, 0
    for instruction in split_dirs(directions):
        dx, dy = HEADINGS[instruction]
        x += dx
        y += dy
    return x, y


def main():
    tiles = set()
    with open("directions.txt") as f:
        tiles_to_flip = (get_pos(line.strip()) for line in f)
        for tile in tiles_to_flip:
            if tile in tiles:
                tiles.remove(tile)
            else:
                tiles.add(tile)

    print(len(tiles))


if __name__ == "__main__":
    main()
