from collections import deque

import numpy as np


def adj(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


def main():
    f = [
        "###########",
        "#0.1.....2#",
        "#.#######.#",
        "#4.......3#",
        "###########",
    ]
    with open("roof.txt") as f:
        roof_map = np.array([list(line.strip()) for line in f])

    n_locs = 0
    for i in range(roof_map.shape[0]):
        for j in range(roof_map.shape[1]):
            char = roof_map[i, j]
            if char == "0":
                start_pos = (i, j)
            if char.isnumeric():
                n_locs = max(n_locs, int(char))

    done_part1 = False
    seen = set()
    q = deque()
    q.append((0, start_pos, ("0",)))
    while q:
        n_moves, pos, locs_visited = q.popleft()
        if (pos, locs_visited) in seen:
            continue
        seen.add((pos, locs_visited))
        if len(locs_visited) == n_locs + 1:
            if not done_part1:
                shortest_route_without_return = n_moves
                done_part1 = True
            if roof_map[pos] == "0":
                shortest_route_with_return = n_moves
                break
        for new_pos in adj(*pos):
            char = roof_map[new_pos]
            if char != "#":
                if char.isnumeric() and char not in locs_visited:
                    new_locs_visited = tuple(sorted(locs_visited + (char,)))
                    q.append((n_moves + 1, new_pos, new_locs_visited))
                else:
                    q.append((n_moves + 1, new_pos, locs_visited))

    print(shortest_route_without_return)
    print(shortest_route_with_return)


if __name__ == "__main__":
    import time
    start = time.time()
    main()
    print(time.time() - start)
