from itertools import permutations


DIGITS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def gen_wire_maps():
    segments = "abcdefg"
    for perm in permutations(segments):
        yield dict(zip(perm, segments))


def apply_map(pattern, wire_map):
    return "".join(sorted(map(wire_map.get, pattern)))


def check_map(patterns, wire_map):
    return {apply_map(pat, wire_map) for pat in patterns} == DIGITS.keys()


def decode(patterns, outputs):
    segments = "abcdefg"
    for wire_map in gen_wire_maps():
        if check_map(patterns, wire_map):
            return [DIGITS[apply_map(out, wire_map)] for out in outputs]


def main():
    with open("lights.txt") as f:
        total = 0
        for line in f:
            patterns, outputs = (chunk.split() for chunk in line.strip().split(" | "))
            total += int("".join(map(str, decode(patterns, outputs))))
        print(total)


if __name__ == "__main__":
    main()
