from functools import cache


def main():
    with open("patterns.txt") as f:
        available = next(f).strip().split(", ")
        next(f)
        desired = [line.strip() for line in f]

    @cache
    def count_the_ways(target):
        if target == "":
            return 1

        return sum(
            count_the_ways(target[len(option):])
            for option in available
            if target.startswith(option)
        )

    part_1 = part_2 = 0
    for pattern in desired:
        count = count_the_ways(pattern)
        part_1 += count > 0
        part_2 += count
    print(part_1)
    print(part_2)


if __name__ == "__main__":
    main()
