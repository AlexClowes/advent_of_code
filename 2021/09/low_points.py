import numpy as np


def main():
    with open("heightmap.txt") as f:
        heightmap = np.array([[int(char) for char in line.strip()] for line in f])


    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < heightmap.shape[0] - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < heightmap.shape[1] - 1:
            yield i, j + 1


    def is_low(i, j):
        return all(heightmap[i, j] < heightmap[a] for a in adj(i, j))


    total_risk = sum(
        1 + heightmap[i, j] for i, j in np.ndindex(heightmap.shape) if is_low(i, j)
    )
    print(total_risk)


if __name__ == "__main__":
    main()
