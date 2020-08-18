import numpy as np

from numba import njit


@njit
def max_power_loc(fuel, size):
    max_power = -999999
    for i in range(fuel.shape[0] - size + 1):
        for j in range(fuel.shape[1] - size + 1):
            power = np.sum(fuel[i : i + size, j : j + size])
            if power > max_power:
                max_power = power
                x, y = j + 1, i + 1
    return max_power, x, y


def main():
    serial_no = 1309
    x = np.arange(1, 301).reshape(1, 300)
    fuel = ((x + 10) * x.T + serial_no) * (x + 10)
    fuel = (fuel // 100) % 10 - 5

    _, x, y = max_power_loc(fuel, 3)
    print(x, y, sep=",")

    max_power = 0
    for size in range(1, 301):
        power, x, y = max_power_loc(fuel, size)
        if power > max_power:
            max_power = power
            ret = x, y, size
    print(*ret, sep=",")


if __name__ == "__main__":
    main()
