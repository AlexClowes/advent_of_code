from collections import Counter, deque
from itertools import combinations, permutations, product
from functools import cached_property


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

    def __add__(self, other):
        return Vector(*((s + o) for s, o in zip(self, other)))

    def __sub__(self, other):
        return Vector(*((s - o) for s, o in zip(self, other)))

    def __neg__(self):
        return Vector(*(-c for c in self))

    def rotate(self, mat):
        return Vector(
            *(sum(r * c for r, c in zip(row, self.components)) for row in mat)
        )


class Report:
    def __init__(self, beacons):
        self.beacons = list(beacons)

    def __iter__(self):
        return iter(self.beacons)

    @cached_property
    def fingerprint(self):
        return Counter(abs(x - y) for x, y in combinations(self, 2))

    @cached_property
    def displacements(self):
        return Counter(x - y for x, y in permutations(self, 2))

    def rotate(self, rotation):
        return Report(
            [beacon.rotate(rotation) for beacon in self],
        )

    def translate(self, translation):
        return Report(
            [beacon + translation for beacon in self],
        )


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
            Report(
                Vector(*map(int, line.split(","))) for line in report.split("\n")[1:]
            )
            for report in f.read().strip().split("\n\n")
        ]

    def significant_overlap(reference, candidate):
        f1 = reference.fingerprint
        f2 = candidate.fingerprint
        return (
            sum(min(f1[k], f2[k]) for k in f1)
            >= shared_beacons * (shared_beacons - 1) // 2
        )

    def match_rotation(reference, candidate):
        d1 = reference.displacements
        for rotation in rotations:
            rotated = candidate.rotate(rotation)
            d2 = rotated.displacements
            if sum(min(d1[k], d2[k]) for k in d1) >= shared_beacons * (shared_beacons - 1):
                return rotated
        return False

    def match_translation(reference, candidate):
        translation, count = Counter(
            b1 - b2 for b1 in reference for b2 in candidate
        ).most_common(1)[0]
        if count >= shared_beacons:
            return candidate.translate(translation), translation
        return False

    beacons = set(reports[0])
    unaligned = set(reports[1:])
    scanners = {Vector(0, 0, 0)}
    q = [reports[0]]
    while q:
        reference = q.pop(0)
        for candidate in set(unaligned):
            if (
                significant_overlap(reference, candidate)
                and (rotated := match_rotation(reference, candidate))
                and (result := match_translation(reference, rotated))
            ):
                translated, translation = result
                beacons.update(translated)
                unaligned.remove(candidate)
                q.append(translated)
                scanners.add(translation)

    # Part 1
    print(len(beacons))
    # Part 2
    print(max(manhattan_distance(s1, s2) for s1 in scanners for s2 in scanners))


if __name__ == "__main__":
    main()
