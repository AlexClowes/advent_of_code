def main():
    with open("ingredients.txt") as f:
        fresh_ranges = []
        for line in f:
            if not line.strip():
                break
            start, end = map(int, line.split("-"))
            fresh_ranges.append((start, end))

    def intersect(interval_a, interval_b):
        a1, a2 = interval_a
        b1, b2 = interval_b
        return a1 <= b1 <= a2 or a1 <= b2 <= a2 or b1 <= a1 <= b2 or b1 <= a2 <= b2

    def union(interval_a, interval_b):
        return (
            min(interval_a[0], interval_b[0]),
            max(interval_a[1], interval_b[1]),
        )

    def consolidate_ranges():
        nonlocal fresh_ranges
        work_done = False
        new_ranges = []
        for interval_a in fresh_ranges:
            for idx, interval_b in enumerate(new_ranges):
                if intersect(interval_a, interval_b):
                    new_ranges[idx] = union(interval_a, interval_b)
                    work_done = True
                    break
            else:
                new_ranges.append(interval_a)
        fresh_ranges = new_ranges
        return work_done

    while consolidate_ranges():
        pass

    print(sum(hi - lo + 1 for lo, hi in fresh_ranges))


if __name__ == "__main__":
    main()
