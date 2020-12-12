import numpy as np


def rotate_anticlockwise(heading, angle):
    if angle == 90:
        heading[0], heading[1] = -heading[1], heading[0]
    elif angle == 180:
        heading[:] = -heading
    elif angle == 270:
        heading[0], heading[1] = heading[1], -heading[0]
    else:
        raise ValueError(f"Expected angle to be one of 90, 180, 270, but got {angle}")
    return heading


def main():
    with open("directions.txt") as f:
        directions = [(line[0], int(line.strip()[1:])) for line in f]

    heading = np.array([1, 0])
    position = np.array([0, 0])

    displacement = {
        "N": np.array([0, 1]),
        "S": np.array([0, -1]),
        "E": np.array([1, 0]),
        "W": np.array([-1, 0]),
    }
    for op, operand in directions:
        if op in "NSEW":
            position += operand * displacement[op]
        elif op == "L":
            rotate_anticlockwise(heading, operand)
        elif op == "R":
            rotate_anticlockwise(heading, 360 - operand)
        elif op == "F":
            position += operand * heading
        else:
            raise ValueError(f"Unrecognised op {op}")
    print(sum(abs(position)))


if __name__ == "__main__":
    main()
