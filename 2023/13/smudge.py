def get_patterns(f):
    pattern = []
    for line in f:
        if row := line.strip():
            pattern.append(list(row))
        else:
            yield pattern
            pattern.clear()
    yield pattern


def transpose(pattern):
    return list(zip(*pattern))


def get_horizontal_mirror(pattern):
    for i in range(1, len(pattern)):
        if all(
            above == below
            for above, below in zip(reversed(pattern[:i]), pattern[i:])
        ):
            yield i


def get_vertical_mirror(pattern):
    yield from get_horizontal_mirror(transpose(pattern))


def flip(char):
    if char == ".":
        return "#"
    return "."


def vary(pattern):
    for i, row in enumerate(pattern):
        for j, char in enumerate(row):
            pattern[i][j] = flip(pattern[i][j])
            yield pattern
            pattern[i][j] = flip(pattern[i][j])


def main():
    with open("patterns.txt") as f:
        total = 0
        for pattern in get_patterns(f):
            original_vert = next(get_vertical_mirror(pattern), None)
            original_horiz = next(get_horizontal_mirror(pattern), None)

            for pattern_var in vary(pattern):
                new_vert = next(
                    (
                        idx
                        for idx in get_vertical_mirror(pattern_var)
                        if idx != original_vert
                    ),
                    None
                )
                if new_vert:
                    total +=  new_vert
                    break
                new_horiz = next(
                    (
                        idx
                        for idx in get_horizontal_mirror(pattern_var)
                        if idx != original_horiz
                    ),
                    None
                )
                if new_horiz:
                    total +=  100 * new_horiz
                    break
        print(total)


if __name__ == "__main__":
    main()
