from itertools import count

import numpy as np
from scipy.spatial.distance import cdist


def main():
    with open("racetrack.txt") as f:
        arr = np.array([list(line.strip()) for line in f])
    height, width = arr.shape

    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < height - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < width - 1:
            yield i, j + 1

    track = []
    seen = set()
    pos = next(pos for pos, char in np.ndenumerate(arr) if char == "S")
    for idx in count():
        track.append(pos)
        if arr[pos] == "E":
            break
        seen.add(pos)
        pos = next(
            pos for pos in adj(*pos) if pos not in seen and arr[pos] in ".E"
        )
    track = np.array(track)

    dist = np.triu(cdist(track, track, "cityblock"))
    r = np.arange(len(track))
    big_saving = (r - r[:, np.newaxis] - dist) >= 100

    print(((dist == 2) & big_saving).sum())
    print(((dist <= 20) & big_saving).sum())
    

if __name__ == "__main__":
    main()
