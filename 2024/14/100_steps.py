import numpy as np
import re


def main():
    dims = np.array([101, 103])
    with open("initial_state.txt") as f:
        state = np.array(
            [
                [
                    int(n) for n in 
                    re.match("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups()
                ]
                for line in f
            ]
        )
        pos = state[:, :2]
        vel = state[:, 2:]

    pos = (pos + 100 * vel) % dims
    
    mid_x, mid_y = dims // 2
    left = pos[:, 0] < mid_x
    right = pos[:, 0] > mid_x
    top = pos[:, 1] < mid_y
    bottom = pos[:, 1] > mid_y
    print(
        np.sum(left & top)
        * np.sum(left & bottom)
        * np.sum(right & top)
        * np.sum(right & bottom)
    )


if __name__ == "__main__":
    main()
