from collections import defaultdict, deque
import numpy as np


def main():
    with open("garden.txt") as f:
        arr = np.array([list(line.strip()) for line in f])
    arr = np.pad(arr, 1, constant_values=".")

    i_max, j_max = arr.shape

    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < i_max - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < j_max - 1:
            yield i, j + 1

    covered = set()

    def get_area_fences(start):
        area = 0
        fences = set()
        plant = arr[start]
        q = deque([start])
        seen = set()
        while q:
            pos = q.popleft()
            if pos in seen:
                continue
            seen.add(pos)
            if arr[pos] == plant:
                area += 1
                covered.add(pos)
                for adj_pos in adj(*pos):
                    q.append(adj_pos)
                    if arr[adj_pos] != plant:
                        fences.add(((pos, arr[pos]), (adj_pos, arr[adj_pos])))
        return area, fences

    def consecutive_runs(nums):
        runs = 1
        last = nums[0]
        for n in nums[1:]:
            if n != last + 1:
                runs += 1
            last = n
        return runs

    def count_sides(fences):
        sides = defaultdict(set)
        for fence in fences:
            ((i1, j1), p1), ((i2, j2), p2) = sorted(fence)
            if i1 == i2:
                sides["v", j1, p1, p2].add(i1)
            else:
                sides["h", i1, p1, p2].add(j1)

        for o1, i1, p11, p12 in list(sides):
            for o2, i2, p21, p22 in list(sides):
                if o1 == o2 and i1 == i2 and ((p11 == p21) ^ (p12 == p22)):
                    sides[o1, i1, p11, p12] |= sides[o2, i2, p21, p22]
                    del sides[o2, i2, p21, p22]

        return sum(consecutive_runs(sorted(v)) for v in sides.values())

    part1 = part2 = 0
    for i in range(1, i_max - 1):
        for j in range(1, j_max - 1):
            if (i, j) not in covered:
                area, fences = get_area_fences((i, j))
                part1 += area * len(fences)
                part2 += area * count_sides(fences)
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
