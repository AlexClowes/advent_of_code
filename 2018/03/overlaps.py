import re

import numpy as np


def main():
    pat = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
    with open("claims.txt") as f:
        claims = [[int(n) for n in re.match(pat, line).groups()] for line in f]

    fabric = np.zeros((1000, 1000))
    for _, i, j, x, y in claims:
        fabric[i:i+x, j:j+y] += 1
    print(np.sum(fabric > 1))

    for claim_id, i, j, x, y in claims:
        if (fabric[i:i+x, j:j+y] == 1).all():
            print(claim_id)
            break


if __name__ == "__main__":
    main()
