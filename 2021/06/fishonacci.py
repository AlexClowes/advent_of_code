import numpy as np


def fish_count(initial_state, n_days):
    mat = np.diag(np.ones(8, dtype=int), 1)
    mat[6, 0] = mat[8, 0] = 1
    return np.linalg.matrix_power(mat, n_days).dot(initial_state).sum()


def main():
    with open("fish.txt") as f:
        initial_state = np.zeros(9, dtype=int)
        for x in f.read().strip().split(","):
            initial_state[int(x)] += 1

    print(fish_count(initial_state, 80))
    print(fish_count(initial_state, 256))


if __name__ == "__main__":
    main()
