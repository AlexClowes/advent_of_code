import heapq

import numpy as np


def low_risk_path(risk):
    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < risk.shape[0] - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < risk.shape[1] - 1:
            yield i, j + 1

    start = (0, 0)
    end = (risk.shape[0] - 1, risk.shape[1] - 1)

    seen = set()
    q = [(0, start)]
    while q:
        total_risk, pos = heapq.heappop(q)
        if pos in seen:
            continue
        seen.add(pos)
        if pos == end:
            return total_risk
        for new_pos in adj(*pos):
            heapq.heappush(q, (total_risk + risk[new_pos], new_pos))


def embiggen_risk(risk):
    def update_risk(risk):
        new_risk = risk.copy()
        new_risk += 1
        new_risk[new_risk > 9] = 1
        return new_risk

    H, W = risk.shape
    big_risk = np.zeros((5 * H, 5 * W), dtype=risk.dtype)
    big_risk[:H, :W] = risk
    # Top row
    for j in range(1, 5):
        big_risk[:H, j * W : (j + 1) * W] = update_risk(big_risk[:H, (j - 1) * W : j * W])
    # Other rows
    for i in range(1, 5):
        for j in range(5):
            big_risk[i * H : (i + 1) * H, j * W : (j + 1) * W] = update_risk(
                big_risk[(i - 1) * H : i * H, j * W : (j + 1) * W]
            )
    return big_risk


def main():
    with open("risk_level.txt") as f:
        risk = np.array([[int(char) for char in line.strip()] for line in f])

    # Part 1
    print(low_risk_path(risk))
    # Part 2
    print(low_risk_path(embiggen_risk(risk)))


if __name__ == "__main__":
    main()
