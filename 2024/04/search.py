import numpy as np


def main():
    with open("wordsearch.txt") as f:
        wordsearch = np.array([list(line.strip()) for line in f])

    i_max, j_max = wordsearch.shape

    count = 0
    # horizontal
    for i in range(i_max):
        for j in range(j_max - 3):
            if "".join(wordsearch[i, j : j + 4]) in ("XMAS", "SAMX"):
                count += 1
    # vertical
    for i in range(i_max - 3):
        for j in range(j_max):
            if "".join(wordsearch[i : i + 4, j]) in ("XMAS", "SAMX"):
                count += 1

    # diagonal
    for i in range(i_max - 3):
        for j in range(j_max - 3):
            if "".join(wordsearch[i + k, j + k] for k in range(4)) in ("XMAS", "SAMX"):
                count += 1
    for i in range(3, i_max):
        for j in range(j_max - 3):
            if "".join(wordsearch[i - k, j + k] for k in range(4)) in ("XMAS", "SAMX"):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
