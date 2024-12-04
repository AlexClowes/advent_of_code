import numpy as np


def matches(subarr):
    diag_1 = ((0, 0), (1, 1), (2, 2))
    diag_2 = ((0, 2), (1, 1), (2, 0))

    def get_str(indices):
        return "".join(subarr[idx] for idx in indices)

    return {get_str(diag_1), get_str(diag_2)} <= {"MAS", "SAM"}


def main():
    with open("wordsearch.txt") as f:
        wordsearch = np.array([list(line.strip()) for line in f])

    i_max, j_max = wordsearch.shape

    count = 0
    for i in range(i_max - 2):
        for j in range(j_max - 2):
            if matches(wordsearch[i : i + 3, j : j + 3]):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
