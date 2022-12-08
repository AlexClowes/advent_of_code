import numpy as np


def count_visible(tree_heights):
    visible = np.zeros_like(tree_heights, dtype=bool)

    for _ in range(4):
        tree_heights, visible = np.rot90(tree_heights), np.rot90(visible)
        visible[0] = True
        visible[1:] |= np.diff(np.maximum.accumulate(tree_heights, axis=0), axis=0) > 0

    return visible.sum()


def main():
    with open("map.txt") as f:
        tree_heights = np.array([[int(h) for h in line.strip()] for line in f])
    print(count_visible(tree_heights))


if __name__ == "__main__":
    main()
