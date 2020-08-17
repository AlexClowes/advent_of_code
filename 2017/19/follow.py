import numpy as np


def left(i, j):
    return (-j, i)

def right(i, j):
    return (j, -i)


def follow(trail):
    in_bounds = lambda i, j: all(0 <= (i, j)[n] < trail.shape[n] for n in (0, 1))

    # Get start position
    i, j = 0, 0
    while trail[0, j] != "|":
        j += 1

    total_steps = 0
    current_dir = 1, 0
    while in_bounds(i, j) and trail[i, j] != " ":
        total_steps += 1
        char = trail[i, j]
        if char.isalpha():
            yield char
        if trail[i, j] == "+":
            # Need to pick a new direction
            for new_dir in (left(*current_dir), right(*current_dir)):
                new_pos = (i + new_dir[0], j + new_dir[1])
                if in_bounds(*new_pos) and trail[new_pos] != " ":
                    i, j = new_pos
                    current_dir = new_dir
                    break
        else:
            # Continue as before
            i += current_dir[0]
            j += current_dir[1]
    print(total_steps)


def main():
    with open("trail.txt") as f:
        trail = np.array([list(line[:-1]) for line in f])
    print("".join(follow(trail)))


if __name__ == "__main__":
    main()
