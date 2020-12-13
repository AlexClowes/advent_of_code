def extended_gcd(a, b):
    """
    Given coprime a, b uses extended euclidean algorithm to compute s, t s.t.
    a * s + b * t = 1
    """
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return s0, t0


def chinese_remainder_theorem(n1, a1, n2, a2):
    """
    Compute smallest positive solution to congruences
    x = a1 (mod n1)
    x = a2 (mod n2)
    where n1, n2 are coprime.
    """
    m1, m2 = extended_gcd(n1, n2)
    return (a1 * m2 * n2 + a2 * m1 * n1) % (n1 * n2)


def main():
    with open("timetable.txt") as f:
        f.readline()
        id_offset = [
            (int(id), -i)
            for (i, id) in enumerate(f.readline().strip().split(","))
            if id != "x"
        ]

    tn, ta = 1, 0
    for n, a in id_offset:
        ta = chinese_remainder_theorem(tn, ta, n, a)
        tn *= n
    print(ta)


if __name__ == "__main__":
    main()
