from collections import defaultdict, deque

import numpy as np


def adjacent(i, j):
    yield i + 1, j
    yield i - 1, j
    yield i, j + 1
    yield i, j - 1


def isalpha(arr):
    return "".join(arr).isalpha()


def get_portals(maze):
    portals = defaultdict(list)
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if isalpha(maze[i, j : j + 2]):
                name = "".join(maze[i, j : j + 2])
                if j + 2 < maze.shape[1] and maze[i, j + 2] == ".":
                    portals[name].append((i, j + 2))
                elif j - 1 > 0 and maze[i, j - 1] == ".":
                    portals[name].append((i, j - 1))
            elif isalpha(maze[i : i + 2, j]):
                name = "".join(maze[i : i + 2, j])
                if i + 2 < maze.shape[0] and maze[i + 2, j] == ".":
                    portals[name].append((i + 2, j))
                elif i - 1 > 0 and maze[i - 1, j] == ".":
                    portals[name].append((i - 1, j))
    return portals


def get_portal_locs(maze, name):
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if j < maze.shape[1] - 1 and "".join(maze[i, j : j + 2]) == name:
                return i, j - 1 if j > 0 and maze[i, j - 1] == "." else i, j + 3
            if i < maze.shape[1] - 1 and "".join(maze[i : i + 2, j]) == name:
                return i - 1, j if i > 0 and maze[i - 1, j] == "." else i + 3, j


def shortest_path(maze):
    start = get_portal_loc(maze, "AA")
    end = get_portal_loc(maze, "ZZ")
    portals = get_portals(maze)

    # BFS
    seen = {portals["AA"][0]}
    queue = deque()
    queue.append((portals["AA"][0], 0))
    while queue:
        pos, dist = queue.popleft()
        for adj in adjacent(*pos):
            if maze[adj] == portals["ZZ"]
            if maze[adj] == ".":
                queue.append((adj, dist + 1))





def main():
    maze = [
        "         A         ", 
        "         A         ",
        "  #######.#########",  
        "  #######.........#",  
        "  #######.#######.#",  
        "  #######.#######.#",  
        "  #######.#######.#",  
        "  #####  B    ###.#",  
        "BC...##  C    ###.#",  
        "  ##.##       ###.#",  
        "  ##...DE  F  ###.#",  
        "  #####    G  ###.#",  
        "  #########.#####.#",  
        "DE..#######...###.#",  
        "  #.#########.###.#",  
        "FG..#########.....#",  
        "  ###########.#####",  
        "             Z     ",  
        "             Z     ",  
    ]
    maze = np.array([list(line) for line in maze])

    print(shortest_path(maze))


if __name__ == "__main__":
    main()
