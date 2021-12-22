from collections import Counter
from itertools import permutations, product

import numpy as np


class Vector:
    def __init__(self, *components):
        self.components = components

    def __hash__(self):
        return hash(self.components)

    def __eq__(self, other):
        return self.components == other.components

    def __iter__(self):
        yield from self.components

    def __abs__(self):
        return sum(c * c for c in self.components)

    def __sub__(self, other):
        return Vector(*(s - o for s, o in zip(self, other)))

    def __neg__(self):
        return Vector(*(-c for c in self))

    def rotate(self, mat):
        return Vector(*(sum(r * c for r, c in zip(row, self.components)) for row in mat))


def get_rotations():
    rotations = []
    for i, j, k in permutations(range(3), 3):
        for s1, s2 in product((1, -1), repeat=2):
            rot = [[0 for _ in range(3)] for _ in range(3)]
            rot[i][0] = s1
            rot[j][1] = s2
            # Cross product
            rot[k][2] = s1 * s2 * (1 if (i + 1) % 3 == j else -1)
            rotations.append(rot)
    return rotations


def manhattan_distance(vec1, vec2):
    return sum(abs(diff) for diff in vec1 - vec2)


def main():
    shared_beacons = 12
    rotations = get_rotations()
    with open("scanner_reports.txt") as f:
        reports = [
            tuple(Vector(*map(int, line.split(","))) for line in report.split("\n")[1:])
            for report in f.read().strip().split("\n\n")
        ]

    def significant_overlap(candidate):
        c1 = Counter(abs(x - y) for x, y in permutations(beacons, 2))
        c2 = Counter(abs(x - y) for x, y in permutations(candidate, 2))
        return sum(min(c1[k], c2[k]) for k in c2) >= shared_beacons * (shared_beacons - 1)

    def match_rotation(candidate):
        c1 = Counter(x - y for x, y in permutations(beacons, 2))
        for rotation in rotations:
            rotated = [beacon.rotate(rotation) for beacon in candidate]
            c2 = Counter(x - y for x, y in permutations(rotated, 2))
            if sum(min(c1[k], c2[k]) for k in c2) >= shared_beacons * (shared_beacons - 1):
                return rotated
        return False

    def match_translation(candidate):
        # print(sorted(Counter(b2 - b1 for b1 in beacons for b2 in candidate).values()))
        translation, count = Counter(
            b2 - b1 for b1 in beacons for b2 in candidate
        ).most_common(1)[0]
        if count >= shared_beacons:
            return [beacon - translation for beacon in candidate], translation
        return False

    beacons = set(reports[0])
    scanners = set()
    reports = reports[1:]
    while reports:
        candidate = reports.pop(0)
        if (
            significant_overlap(candidate)
            and (rotated := match_rotation(candidate))
            and (result := match_translation(rotated))
        ):
            translated, translation = result
            beacons.update(translated)
            scanners.add(-translation)
        else:
            reports.append(candidate)

    # Part 1
    print(len(beacons))
    # Part 2
    print(max(manhattan_distance(s1, s2) for s1 in scanners for s2 in scanners))


if __name__ == "__main__":
    main()
