import numpy as np


def main():
    with open("seafloor.txt") as f:
        arr = np.array([list(line.strip()) for line in f])

    def move(char, axis):
        will_move = (arr == char) & (np.roll(arr, -1, axis=axis) == ".")
        arr[will_move] = "."
        arr[np.roll(will_move, 1, axis=axis)] = char
        return will_move.any()

    steps = 1
    while move(">", 1) | move("v", 0):
        steps += 1
    print(steps)


if __name__ == "__main__":
    main()
