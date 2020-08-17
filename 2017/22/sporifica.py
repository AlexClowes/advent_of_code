import numpy as np


def get_infected_nodes(map_file_loc):
    with open("map.txt") as f:
        grid = np.array([[".#".find(c) for c in line.strip()] for line in f])

    infected_nodes = set()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j]:
                infected_nodes.add((j - grid.shape[1] // 2, grid.shape[0] // 2 - i))
    return infected_nodes


def right(direction):
    return (direction[1], -direction[0])


def left(direction):
    return (-direction[1], direction[0])


def main():
    infected_nodes = get_infected_nodes("map.txt")
    pos = (0, 0)
    direction = (0, 1)
    infections_caused = 0
    for _ in range(10 ** 4):
        if pos in infected_nodes:
            direction = right(direction)
            infected_nodes.remove(pos)
        else:
            direction = left(direction)
            infected_nodes.add(pos)
            infections_caused += 1
        pos = (pos[0] + direction[0], pos[1] + direction[1])

    print(infections_caused)


if __name__ == "__main__":
    main()
