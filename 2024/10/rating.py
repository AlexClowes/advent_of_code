from collections import deque
import numpy as np


def main():
    with open("topography.txt") as f:
        arr = np.array([[int(n) for n in line.strip()] for line in f])

    i_max = len(arr)
    j_max = len(arr[0])

    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < i_max - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < j_max - 1:
            yield i, j + 1

    graph = {
        pos: {adj_pos for adj_pos in adj(*pos) if arr[adj_pos] == height + 1}
        for pos, height in np.ndenumerate(arr)
    }

    def score(trailhead):
        ret = 0
        q = deque([trailhead])
        while q:
            pos = q.popleft()
            if arr[pos] == 9:
                ret += 1
            else:
                q.extend(graph[pos])
        return ret

    print(sum(score(pos) for pos, height in np.ndenumerate(arr) if height == 0))


if __name__ == "__main__":
    main()
