from collections import namedtuple


class Vector(namedtuple("Vector", ("x", "y"))):
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return max(abs(self.x), abs(self.y))


def gen_moves(file):
    headings = {
        "U": Vector(0, 1),
        "D": Vector(0, -1),
        "L": Vector(-1, 0),
        "R": Vector(1, 0),
    }
    with open(file) as f:
        for line in f:
            heading, count = line.strip().split()
            yield headings[heading], int(count)


def sgn(x):
    return -1 if x < 0 else 0 if x == 0 else 1


def update_tail(head, tail):
    diff = head - tail
    if abs(diff) <= 1:
        return tail
    dx, dy = diff
    return tail + Vector(sgn(dx), sgn(dy))


def simulate_rope(rope, moves):
    for heading, distance in moves:
        for _ in range(distance):
            rope[0] += heading
            for i in range(1, len(rope)):
                rope[i] = update_tail(rope[i - 1], rope[i])
            yield rope


def main():
    for rope_len in (2, 10):
        visited = set()
        initial_rope = [Vector(0, 0) for _ in range(rope_len)]

        for rope_state in simulate_rope(initial_rope, gen_moves("moves.txt")):
            visited.add(rope_state[-1])
        print(len(visited))


if __name__ == "__main__":
    main()
