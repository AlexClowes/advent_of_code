def sign(x):
    return x / abs(x) if x != 0 else 0


def is_safe(report):
    direction = sign(report[1] - report[0])
    if direction == 0:
        return False
    diffs = (r1 - r0 for r0, r1 in zip(report, report[1:]))
    return all(
        1 <= abs(diff) <= 3 and sign(diff) == direction
        for diff in diffs
    )


def main():
    with open("levels.txt") as f:
        reports = ([int(level) for level in line.strip().split()] for line in f)
        print(sum(is_safe(report) for report in reports))


if __name__ == "__main__":
    main()
