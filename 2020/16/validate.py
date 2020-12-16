from itertools import chain
import re


def main():
    field_ranges = []
    with open("tickets.txt") as f:
        # Get field ranges
        while (line := f.readline()) != "\n":
            pat = r"[\w\s]+: (\d+)-(\d+) or (\d+)-(\d+)"
            lo1, hi1, lo2, hi2 = map(int, re.match(pat, line).groups())
            field_ranges += [range(lo1, hi1 + 1), range(lo2, hi2 + 1)]

        # Your ticket
        assert f.readline() == "your ticket:\n"
        f.readline()
        assert f.readline() == "\n"

        # Nearby tickets
        assert f.readline() == "nearby tickets:\n"
        nearby_tickets = (map(int, line.strip().split(",")) for line in f)

        print(
            sum(
                n
                for n in chain.from_iterable(nearby_tickets)
                if all(n not in r for r in field_ranges)
            )
        )


if __name__ == "__main__":
    main()
