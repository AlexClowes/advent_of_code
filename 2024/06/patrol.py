import numpy as np


def turn_right(di, dj):
    return dj, -di


def add(tup1, tup2):
    return tuple(x + y for x, y in zip(tup1, tup2))


def main():
    with open("map.txt") as f:
        arr = np.array([list(line.strip()) for line in f])

    guard_pos = next((i, j) for (i, j), char in np.ndenumerate(arr) if char == "^")
    arr[guard_pos] = "."
    guard_heading = (-1, 0)

    visited = np.zeros_like(arr, dtype=bool)

    while True:
        visited[guard_pos] = True
        new_pos = add(guard_pos, guard_heading)
        if not 0 <= new_pos[0] < arr.shape[0] and 0 <= new_pos[1] < arr.shape[1]:
            break
        elif arr[new_pos] == ".":
            guard_pos = new_pos
        else:
            guard_heading = turn_right(*guard_heading)

    print(visited.sum())


if __name__ == "__main__":
    main()
