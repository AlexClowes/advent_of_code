import numpy as np


OPEN = 0
TREES = 1
LUMBER = 2


def advance(state):
    def adj(i, j):
        for k in range(i - 1, i + 2):
            if k < 0 or k >= state.shape[0]:
                continue
            for l in range(j - 1, j + 2):
                if l < 0 or l >= state.shape[1] or (k == i and l == j):
                    continue
                yield k, l

    new_state = np.copy(state)
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            if state[i, j] == OPEN:
                if sum(state[a] == TREES for a in adj(i, j)) >= 3:
                    new_state[i, j] = TREES
            elif state[i, j] == TREES:
                if sum(state[a] == LUMBER for a in adj(i, j)) >= 3:
                    new_state[i, j] = LUMBER
            elif state[i, j] == LUMBER:
                if (
                    sum(state[a] == LUMBER for a in adj(i, j)) < 1
                    or sum(state[a] == TREES for a in adj(i, j)) < 1
                ):
                    new_state[i, j] = OPEN
    return new_state


def main():
    with open("initial_state.txt") as f:
        state = np.array([[".|#".find(c) for c in line.strip()] for line in f])

    for i in range(10):
        state = advance(state)
    print(np.sum(state == TREES) * np.sum(state == LUMBER))


if __name__ == "__main__":
    main()
