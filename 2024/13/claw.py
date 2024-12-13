import re

import numpy as np


def to_int_vec(vals):
    return np.array(list(map(int, vals)), dtype=int)


def parse_machine_spec(f):
    a_vec = re.match(r"Button A: X\+(\d+), Y\+(\d+)", f.readline()).groups()
    b_vec = re.match(r"Button B: X\+(\d+), Y\+(\d+)", f.readline()).groups()
    target_vec = re.match(r"Prize: X=(\d+), Y=(\d+)", f.readline()).groups()
    return to_int_vec(a_vec), to_int_vec(b_vec), to_int_vec(target_vec)


def calculate_presses(a_vec, b_vec, target_vec):
    det = a_vec[0] * b_vec[1] - a_vec[1] * b_vec[0]
    adj = np.array([[b_vec[1], -b_vec[0]], [-a_vec[1], a_vec[0]]])
    if np.all(adj.dot(target_vec) % det == 0):
        return adj.dot(target_vec) // det


def main():
    with open("machine_spec.txt") as f:
        part1 = part2 = 0
        while True:
            a_vec, b_vec, target_vec = parse_machine_spec(f)
            if (
                result := calculate_presses(a_vec, b_vec, target_vec)
            ) is not None:
                a, b = result
                if a.is_integer() and b.is_integer():
                    part1 += 3 * a + b
            if (
                result := calculate_presses(a_vec, b_vec, target_vec + 10 ** 13)
            ) is not None:
                a, b = result
                if a.is_integer() and b.is_integer():
                    part2 += 3 * a + b
            if not f.readline():
                break

        print(part1)
        print(part2)


if __name__ == "__main__":
    main()
