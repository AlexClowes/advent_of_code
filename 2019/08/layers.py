import numpy as np


def main():
    with open("image_data.txt") as f:
        data = np.fromiter(f.read().strip(), np.int8).reshape(-1, 6, 25)
    layer = np.argmin(np.sum(data==0, axis=(1, 2)))
    print(np.sum(data[layer]==1) * np.sum(data[layer]==2))


if __name__ == "__main__":
    main()
