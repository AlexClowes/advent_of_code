import numpy as np


class BugScan:
    def __init__(self, state):
        self.state = np.expand_dims(state, axis=0)

    def _adjacent(self, i, j, k):
        # Non-recursive but adjacent
        if j > 0:
            yield self.state[i, j - 1, k]
        if j < 4:
            yield self.state[i, j + 1, k]
        if k > 0:
            yield self.state[i, j, k - 1]
        if k < 4:
            yield self.state[i, j, k + 1]

        # Next level up
        if i < self.state.shape[0] - 1:
            if j == 0:
                yield self.state[i + 1, 1, 2]
            elif j == 4:
                yield self.state[i + 1, 3, 2]
            if k == 0:
                yield self.state[i + 1, 2, 1]
            elif k == 4:
                yield self.state[i + 1, 2, 3]

        # Next level down
        if i > 0:
            if (j, k) == (1, 2):
                yield from self.state[i - 1, 0, :]
            elif (j, k) == (3, 2):
                yield from self.state[i - 1, -1, :]
            elif (j, k) == (2, 1):
                yield from self.state[i - 1, :, 0]
            elif (j, k) == (2, 3):
                yield from self.state[i - 1, :, -1]

    def advance(self):
        self.state = np.concatenate((
            np.zeros((int(np.any(self.state[0])), 5, 5), dtype=np.bool),
            self.state,
            np.zeros((int(np.any(self.state[-1])), 5, 5), dtype=np.bool),
        ))
        new_state = np.copy(self.state)

        for i in range(new_state.shape[0]):
            for j in range(5):
                for k in range(5):
                    if (j, k) == (2, 2):
                        continue
                    adjacent_bugs = sum(self._adjacent(i, j, k))
                    if self.state[i, j, k] and adjacent_bugs != 1:
                        new_state[i, j, k] = 0
                    elif not self.state[i, j, k] and adjacent_bugs in [1, 2]:
                        new_state[i, j, k] = 1
        self.state = new_state

    def count(self):
        return np.sum(self.state)


def main():
    with open("scan.txt") as f:
        scan = np.array([[char == "#" for char in line.strip()] for line in f])
    scan = BugScan(scan)

    for _ in range(200):
        scan.advance()
    print(scan.count())


if __name__ == "__main__":
    main()
