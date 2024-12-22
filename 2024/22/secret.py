import numpy as np


MOD = 16777216


def main():
    with open("numbers.txt") as f:
        numbers = np.array([int(line.strip()) for line in f], dtype=np.int32)

    for i in range(2000):
        numbers = (numbers ^ (numbers << 6)) % MOD
        numbers = (numbers ^ (numbers >> 5)) % MOD
        numbers = (numbers ^ (numbers << 11)) % MOD
    print(numbers.sum())


if __name__ == "__main__":
    main()
