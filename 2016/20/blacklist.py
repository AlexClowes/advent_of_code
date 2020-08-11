def main():
    with open("blacklist.txt") as f:
        ranges = [tuple(map(int, line.strip().split("-"))) for line in f]

    ranges = sorted(ranges)

    found_min = False
    if ranges[0][0] != 0:
        min_allowed = 0
        found_min = True
    allowed_count = ranges[0][0]

    max_hi = ranges[0][1]
    for lo, hi in ranges[1:]:
        if lo > max_hi + 1:
            if not found_min:
                min_allowed = max_hi + 1
                found_min = True
            allowed_count += lo - max_hi - 1
        max_hi = max(max_hi, hi)
    allowed_count += 2 ** 32 - 1 - max_hi

    print(min_allowed)
    print(allowed_count)



if __name__ == "__main__":
    main()
