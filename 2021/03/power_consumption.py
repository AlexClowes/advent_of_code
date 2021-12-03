import numpy as np


def binary_to_decimal(bin_array):
    return int("".join(map(str, bin_array)), base=2)


def power_consumption(report):
    gamma_binary = (np.sum(report, axis=0) > len(report) // 2).astype(int)
    gamma = binary_to_decimal(gamma_binary)
    epsilon = binary_to_decimal(1 - gamma_binary)
    return gamma * epsilon


def main():
    with open("report.txt") as f:
        report = np.array([list(map(int, line.strip())) for line in f])

    print(power_consumption(report))


if __name__ == "__main__":
    main()
