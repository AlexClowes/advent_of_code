import numpy as np


def count_visible(heights):
    first, *rest = heights
    if not rest:
        return 0
    for count, tree in enumerate(rest, 1):
        if tree >= first:
            break
    return count


def scenic_score(pos, tree_heights):
    i, j = pos
    return (
        count_visible(tree_heights[i::-1, j])
        * count_visible(tree_heights[i:, j])
        * count_visible(tree_heights[i, j:])
        * count_visible(tree_heights[i, j::-1])
    )


def main():
    with open("map.txt") as f:
        tree_heights = np.array([[int(h) for h in line.strip()] for line in f])
    print(max(scenic_score((i, j), tree_heights) for i in range(tree_heights.shape[0]) for j in range(tree_heights.shape[1])))


if __name__ == "__main__":
    main()
