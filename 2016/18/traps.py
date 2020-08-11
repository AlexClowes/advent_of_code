import numpy as np


def count_safe_spaces(first_row, n_rows):
    size = len(first_row)
    traps = np.zeros((n_rows, size + 2), dtype=np.bool)
    for i, char in enumerate(first_row):
        traps[0, i + 1] = (char == "^")
    for i in range(1, n_rows):
        traps[i, 1:-1] = traps[i - 1, :size] ^ traps[i - 1, 2:]
    return n_rows * size - np.sum(traps)


def main():
    with open("row.txt") as f:
        first_row = f.read().strip()
    print(count_safe_spaces(first_row, 40))
    print(count_safe_spaces(first_row, 400000))


if __name__ == "__main__":
    main()
