def get_patterns(f):
    pattern = []
    for line in f:
        if row := line.strip():
            pattern.append(row)
        else:
            yield pattern
            pattern.clear()
    yield pattern


def transpose(pattern):
    return list(zip(*pattern))


def get_horizontal_mirror(pattern):
    for i in range(len(pattern) - 1):
        if all(
            pattern[i - j] == pattern[i + 1 + j]
            for j in range(min(i + 1, len(pattern) - i - 1))
        ):
            return i + 1
    return None


def get_vertical_mirror(pattern):
    return get_horizontal_mirror(transpose(pattern))


def main():
    with open("patterns.txt") as f:
        total = 0
        for pattern in get_patterns(f):
            if (idx := get_vertical_mirror(pattern)) is not None:
                total += idx
            elif (idx := get_horizontal_mirror(pattern)) is not None:
                total += 100 * idx
        print(total)


if __name__ == "__main__":
    main()
