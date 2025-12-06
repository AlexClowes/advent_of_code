from itertools import chain


def is_valid(_id):
    _id = str(_id)
    if len(_id) % 2 != 0:
        return True
    mid_point = len(_id) // 2
    return _id[:mid_point] != _id[mid_point:]


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
