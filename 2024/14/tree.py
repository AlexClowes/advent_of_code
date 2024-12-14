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
            ],
        )
        pos = state[:, :2]
        vel = state[:, 2:]

    var_score = (
        (pos + np.arange(dims.prod())[..., np.newaxis, np.newaxis] * vel) % dims
    ).var(axis=1).mean(axis=1)
    print(var_score.argmin())


if __name__ == "__main__":
    main()
