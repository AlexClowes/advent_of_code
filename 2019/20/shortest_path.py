from collections import deque

import numpy as np


def adjacent(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def get_label(maze, point):
    i, j = point
    if i >= 2:
        label = "".join(maze[i - 2 : i, j])
        if label.isalpha():
            return label
    if i < maze.shape[0] - 2:
        label = "".join(maze[i + 1 : i + 3, j])
        if label.isalpha():
            return label
    if j >= 2:
        label = "".join(maze[i, j - 2 : j])
        if label.isalpha():
            return label
    if j < maze.shape[1] - 2:
        label = "".join(maze[i, j + 1 : j + 3])
        if label.isalpha():
            return label


def get_start_end_portals(maze):
    pos2label = {}
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if maze[i, j] == ".":
                label = get_label(maze, (i, j))
                if label is not None:
                    if label == "AA":
                        start_pos = i, j
                    elif label == "ZZ":
                        end_pos = i, j
                    else:
                        pos2label[i, j] = label

    portals = {}
    for pos1, label1 in pos2label.items():
        for pos2, label2 in pos2label.items():
            if pos1 != pos2 and label1 == label2:
                portals[pos1] = pos2

    return start_pos, end_pos, portals


def shortest_path(maze):
    start_pos, end_pos, portals = get_start_end_portals(maze)

    queue = deque()
    queue.append((start_pos, 0))
    seen = {start_pos}
    while queue:
        pos, dist = queue.popleft()
        if pos == end_pos:
            return dist
        for adj in adjacent(*pos):
            if maze[adj] == "." and adj not in seen:
                queue.append((adj, dist + 1))
                seen.add(adj)
        if pos in portals:
            adj = portals[pos]
            if adj not in seen:
                queue.append((adj, dist + 1))
                seen.add(adj)

    raise ValueError("Can't find route to exit")


def main():
    with open("maze.txt") as f:
        maze = np.array([list(line) for line in f])

    print(shortest_path(maze))


if __name__ == "__main__":
    main()
