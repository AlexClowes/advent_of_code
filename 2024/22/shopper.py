from collections import defaultdict
import numpy as np


MOD = 16777216


def main():
    with open("numbers.txt") as f:
        secrets = np.array([int(line.strip()) for line in f], dtype=np.int32)

    bananas = np.zeros((len(secrets), 2001), dtype=np.int32)
    bananas[:, 0] = secrets % 10
    for i in range(1, 2001):
        secrets = (secrets ^ (secrets << 6)) % MOD
        secrets = (secrets ^ (secrets >> 5)) % MOD
        secrets = (secrets ^ (secrets << 11)) % MOD
        bananas[:, i] = secrets % 10
    banana_diffs = bananas[:, 1:] - bananas[:, :-1]

    pattern_scores = defaultdict(int)
    for i in range(banana_diffs.shape[0]):
        seen = set()
        for j in range(banana_diffs.shape[1] - 3):
            pattern = tuple(banana_diffs[i, j : j + 4])
            if pattern in seen:
                continue
            seen.add(pattern)
            pattern_scores[pattern] += bananas[i, j + 4]

    print(max(pattern_scores.values()))


if __name__ == "__main__":
    main()
