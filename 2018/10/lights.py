from itertools import count
import re

import numpy as np


def main():
    with open("initial_state.txt") as f:
        initial_state = np.array(
            [[int(n) for n in re.findall(r"-?\d+", line)] for line in f]
        )
    pos = initial_state[:, :2]
    vel = initial_state[:, 2:]

    # The message is probably visible when the bounding box containing all the
    # points has the smallest area
    old_area = float("inf")
    for time in count():
        pos += vel
        x_min, y_min = np.min(pos, axis=0)
        x_max, y_max = np.max(pos, axis=0)
        area = (y_max - y_min) * (x_max - x_min)
        if area > old_area:
            # We've gone too far, go back
            pos -= vel
            break
        old_area = area
    # Display the message
    display = np.zeros((y_max - y_min + 1, x_max - x_min + 1), dtype=np.bool)
    for x, y in pos:
        display[y - y_min, x - x_min] = 1
    print("\n".join("".join(" #"[n] for n in row) for row in display))
    print(time)


if __name__ == "__main__":
    main()
