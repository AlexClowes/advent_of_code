from itertools import chain
from typing import NamedTuple
import re


class Range(NamedTuple):
    start: int
    end: int

    def valid(self):
        return self.start <= self.end

    def translate(self, trans):
        return self.__class__(self.start + trans, self.end + trans)


def apply_single_map(seed_range, source_range, translation):
    yield Range(seed_range.start, min(seed_range.end, source_range.start - 1))
    yield Range(
        max(seed_range.start, source_range.start),
        min(seed_range.end, source_range.end),
    ).translate(translation)
    yield Range(max(seed_range.start, source_range.end + 1), seed_range.end)


def parse_map(f):
    if not re.match("\w+-to-\w+ map:", f.readline()):
        return

    map_ranges = []
    while line := f.readline().strip():
        dest_start, source_start, range_len = map(int, line.split())
        map_ranges.append(
            (
                Range(source_start, source_start + range_len - 1),
                dest_start - source_start,
            )
        )

    def apply_maps(seed_range):
        for source_range, translation in sorted(
            map_ranges, key=lambda range_trans: range_trans[0].start
        ):
            before, middle, after = apply_single_map(
                seed_range, source_range, translation
            )
            if before.valid():
                yield before
            if middle.valid():
                yield middle
            if after.valid():
                seed_range = after
            else:
                return
        if seed_range.valid():
            yield seed_range

    return apply_maps


def main():
    with open("almanac.txt") as f:
        seed_nos = [
            int(n)
            for n in re.match("seeds: ([\d ]+)", f.readline()).group(1).split()
        ]
        seed_ranges = [
            Range(start, start + length - 1)
            for start, length in zip(seed_nos[::2], seed_nos[1::2])
        ]
        f.readline()

        while map_func := parse_map(f):
            seed_ranges = list(
                chain.from_iterable(
                    map_func(seed_range) for seed_range in seed_ranges
                )
            )

        print(min(seed_range.start for seed_range in seed_ranges))


if __name__ == "__main__":
    main()
