from collections import deque

import numpy as np

from shortest_path import adjacent, get_start_end_portals


def is_outer_portal(maze, pos):
    return pos[0] in (2, maze.shape[0] - 3) or pos[1] in (2, maze.shape[1] - 3)


def shortest_path(maze):
    start_pos, end_pos, portals = get_start_end_portals(maze)

    queue = deque()
    queue.append((start_pos, 0, 0))
    seen = {start_pos, 0}
    while queue:
        pos, level, dist = queue.popleft()
        if pos == end_pos and level == 0:
            return dist
        for adj in adjacent(*pos):
            if maze[adj] == "." and (adj, level) not in seen:
                queue.append((adj, level, dist + 1))
                seen.add((adj, level))
        if pos in portals:
            adj = portals[pos]
            if not is_outer_portal(maze, pos):
                if (adj, level + 1) not in seen:
                    queue.append((adj, level + 1, dist + 1))
                    seen.add((adj, level + 1))
            elif level > 0 and (adj, level - 1) not in seen:
                queue.append((adj, level - 1, dist + 1))
                seen.add((adj, level - 1))

    raise ValueError("Can't find route to exit")


def main():
    with open("maze.txt") as f:
        maze = np.array([list(line.strip("\n")) for line in f])

    print(shortest_path(maze))


if __name__ == "__main__":
    main()
