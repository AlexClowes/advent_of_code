from itertools import count

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


def to_string(state):
    return "\n".join("".join(".|#"[n] for n in row) for row in state)


def resource_val(state):
    return np.sum(state == TREES) * np.sum(state == LUMBER)


def main():
    with open("initial_state.txt") as f:
        state = np.array([[".|#".find(c) for c in line.strip()] for line in f])

    state_to_time = {}
    time_to_rv = {}
    for t in count():
        as_string = to_string(state)
        if as_string in state_to_time:
            t0 = state_to_time[as_string]
            print(time_to_rv[(10 ** 9 - t0) % (t - t0) + t0])
            return
        state_to_time[as_string] = t
        time_to_rv[t] = resource_val(state)
        state = advance(state)


if __name__ == "__main__":
    main()
