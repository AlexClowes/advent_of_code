import re


def parse_map(f):
    if not re.match("\w+-to-\w+ map:", f.readline()):
        return

    ranges = []
    while line := f.readline().strip():
        ranges.append(tuple(map(int, line.split())))

    def map_func(n):
        for dest_start, source_start, range_len in ranges:
            if source_start <= n < source_start + range_len:
                return n - source_start + dest_start
        return n

    return map_func


def main():
    with open("almanac.txt") as f:
        seed_nos = [
            int(n)
            for n in re.match("seeds: ([\d ]+)", f.readline()).group(1).split()
        ]
        f.readline()

        while map_func := parse_map(f):
            seed_nos = [map_func(n) for n in seed_nos]

        print(min(seed_nos))


if __name__ == "__main__":
    main()
