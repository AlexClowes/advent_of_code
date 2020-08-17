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


def reverse(direction):
    return (-direction[0], -direction[1])


def main():
    weakened_nodes = set()
    infected_nodes = get_infected_nodes("map.txt")
    flagged_nodes = set()
    pos = (0, 0)
    direction = (0, 1)
    infections_caused = 0
    for _ in range(10 ** 7):
        if pos in weakened_nodes:
            weakened_nodes.remove(pos)
            infected_nodes.add(pos)
            infections_caused += 1
        elif pos in infected_nodes:
            direction = right(direction)
            infected_nodes.remove(pos)
            flagged_nodes.add(pos)
        elif pos in flagged_nodes:
            direction = reverse(direction)
            flagged_nodes.remove(pos)
        else:
            direction = left(direction)
            weakened_nodes.add(pos)
        pos = (pos[0] + direction[0], pos[1] + direction[1])

    print(infections_caused)


if __name__ == "__main__":
    main()
