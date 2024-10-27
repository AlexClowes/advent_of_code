from functools import cache


@cache
def count_the_ways(springs, counts):
    if not springs:
        return not counts
    if not counts:
        return "#" not in springs
    if len(springs) < sum(counts):
        return 0
    if springs[0] == ".":
        return count_the_ways(springs.lstrip("."), counts)
    if springs[0] == "#":
        if "." in springs[:counts[0]]:
            return 0
        if springs[counts[0]] == "#":
            return 0
        return count_the_ways("." + springs[counts[0] + 1:], counts[1:])
    return (
        count_the_ways("." + springs[1:], counts)
        + count_the_ways("#" + springs[1:], counts)
    )


def main():
    with open("records.txt") as f:
        total = 0
        for line in f:
            springs, counts = line.strip().split()
            springs = "?".join(springs for _ in range(5)) + "."
            counts = tuple(int(c) for c in counts.split(",")) * 5
            total += count_the_ways(springs, counts)
        print(total)


if __name__ == "__main__":
    main()
