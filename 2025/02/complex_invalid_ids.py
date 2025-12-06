def chunk(string, size):
    for i in range(0, len(string) - size + 1, size):
        yield string[i : i + size]


def all_same(iterable):
    first = next(iterable)
    return all(item == first for item in iterable)


def is_valid(_id):
    _id = str(_id)
    for size in range(1, len(_id)):
        if len(_id) % size == 0 and all_same(chunk(_id, size)):
            return False
    return True


def main():
    with open("ids.txt") as f:
        id_ranges = (
            tuple(map(int, id_range.split("-")))
            for id_range in f.readline().strip().split(",")
        )

    total = 0
    for lo, hi in id_ranges:
        total += sum(_id for _id in range(lo, hi + 1) if not is_valid(_id))
    print(total)


if __name__ == "__main__":
    main()
