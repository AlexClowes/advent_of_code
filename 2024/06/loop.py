import numpy as np


def turn_right(di, dj):
    return dj, -di


def add(tup1, tup2):
    return tuple(x + y for x, y in zip(tup1, tup2))


def traverse(history, arr):
    guard_pos, guard_heading = history[-1]
    seen = set(history)
    while True:
        history.append((guard_pos, guard_heading))
        seen.add((guard_pos, guard_heading))
        new_pos = add(guard_pos, guard_heading)
        if not (0 <= new_pos[0] < arr.shape[0] and 0 <= new_pos[1] < arr.shape[1]):
            return False, history
        elif arr[new_pos] == ".":
            guard_pos = new_pos
        else:
            guard_heading = turn_right(*guard_heading)
        if (guard_pos, guard_heading) in seen:
            return True, history


def main():
    with open("map.txt") as f:
        arr = np.array([list(line.strip()) for line in f])

    guard_pos = next(pos for pos, char in np.ndenumerate(arr) if char == "^")
    arr[guard_pos] = "."

    _, original_history = traverse([(guard_pos, (-1, 0))], arr)
    blockers = set()
    seen = set()
    for i, (pos, _) in enumerate(original_history):
        if pos != guard_pos and pos not in blockers and pos not in seen:
            seen.add(pos)
            arr[pos] = "#"
            has_loop, _ = traverse(original_history[:i], arr)
            if has_loop:
                blockers.add(pos)
            arr[pos] = "."
    print(len(blockers))


if __name__ == "__main__":
    main()
