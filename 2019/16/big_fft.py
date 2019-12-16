import numpy as np


def main():
    with open("signal.txt") as f:
        signal = f.readline().strip()
    offset = int(signal[:7])

    # Optimisation only works if assertion holds
    assert 2 * offset > len(signal)

    signal = np.fromiter(signal * 10000, dtype=np.int32)[offset:]

    for _ in range(100):
        signal = np.cumsum(signal[::-1])[::-1] % 10
    print("".join(map(str, signal[:8])))


if __name__ == "__main__":
    main()
