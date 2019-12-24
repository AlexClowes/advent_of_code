import numpy as np


class BugScan:
    def __init__(self, state):
        self.state = state
        self.dims = state.shape

    def _adjacent(self, i, j):
        if i > 0:
            yield self.state[i - 1, j]
        if i < self.dims[0] - 1:
            yield self.state[i + 1, j]
        if j > 0:
            yield self.state[i, j - 1]
        if j < self.dims[1] - 1:
            yield self.state[i, j + 1]

    def advance(self):
        new_state = np.copy(self.state)
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                adjacent_bugs = sum(self._adjacent(i, j))
                if self.state[i, j] and adjacent_bugs != 1:
                    new_state[i, j] = 0
                elif not self.state[i, j] and adjacent_bugs in [1, 2]:
                    new_state[i, j] = 1
        self.state = new_state

    def rating(self):
        ret = 0
        for val in self.state.flatten()[::-1]:
            ret <<= 1
            ret += val
        return ret


def main():
    with open("scan.txt") as f:
        scan = np.array([[char == "#" for char in line.strip()] for line in f])
    scan = BugScan(scan)

    biodiversity_ratings = set()
    rating = scan.rating()
    while rating not in biodiversity_ratings:
        biodiversity_ratings.add(rating)
        scan.advance()
        rating = scan.rating()
    print(rating)


if __name__ == "__main__":
    main()
