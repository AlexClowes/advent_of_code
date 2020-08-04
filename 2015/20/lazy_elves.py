import numpy as np


def main():
    N = 10 ** 6
    n_presents = np.zeros(N)
    for i in range(1, N):
        n_presents[:51 * i:i] += 11 * i
    for i in range(1, N):
        if n_presents[i] > 36000000:
            print(i)
            break


if __name__ == "__main__":
    main()
