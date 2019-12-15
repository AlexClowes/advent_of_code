from collections import defaultdict
from queue import Queue
from threading import Thread

from computer import int_code_computer


WALL = 0
EMPTY = 1
OXYGEN = 2
UNSEEN = 3


def draw_maze(maze):
    tileset = {WALL: "\u2588", EMPTY: ".", OXYGEN: "O", UNSEEN: " "}
    xmin, xmax, ymin, ymax = 0, 0, 0, 0
    for x, y in maze.keys():
        xmin = min(xmin, x)
        xmax = max(xmax, x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)
    x_vals = range(xmin, xmax + 1)
    y_vals = range(ymin, ymax + 1)
    print("-" * len(x_vals))
    lines = ("".join(tileset[maze[x, y]] for x in x_vals) for y in y_vals)
    print("\n".join(lines))
    print("-" * len(x_vals))


def adjacent(pos):
    yield (pos[0], pos[1] - 1)
    yield (pos[0], pos[1] + 1)
    yield (pos[0] - 1, pos[1])
    yield (pos[0] + 1, pos[1])


def flood_fill(maze, pos, input_queue, output_queue):
    opposite = {1: 2, 2: 1, 3: 4, 4: 3}
    for command, new_pos in enumerate(adjacent(pos), 1):
        if maze[new_pos] == UNSEEN:
            input_queue.put(command)
            maze[new_pos] = output_queue.get()
            if maze[new_pos] != WALL:
                flood_fill(maze, new_pos, input_queue, output_queue)
                input_queue.put(opposite[command])
                output_queue.get()


def find_oxygen(maze, pos, dist, visited):
    visited.add(pos)
    if maze[pos] == OXYGEN:
        return dist
    for new_pos in adjacent(pos):
        if new_pos not in visited and maze[new_pos] != WALL:
            ret = find_oxygen(maze, new_pos, dist + 1, visited)
            if ret is not None:
                return ret


def propagate_oxygen(maze):
    oxygen_boundary = {pos for pos in maze if maze[pos] == OXYGEN}
    duration = 0
    while oxygen_boundary:
        new_boundary = set()
        for pos in oxygen_boundary:
            for new_pos in adjacent(pos):
                if maze[new_pos] == EMPTY:
                    maze[new_pos] = OXYGEN
                    new_boundary.add(new_pos)
        oxygen_boundary = new_boundary
        duration += 1
    return duration - 1


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]

    input_queue = Queue()
    output_queue = Queue()
    Thread(target=int_code_computer, args=(program, input_queue, output_queue)).start()

    maze = defaultdict(lambda: UNSEEN)
    pos = (0, 0)
    maze[pos] = EMPTY
    flood_fill(maze, pos, input_queue, output_queue)
    draw_maze(maze)

    print(find_oxygen(maze, (0, 0), 0, set()))

    print(propagate_oxygen(maze))

    input_queue.put(StopIteration)


if __name__ == "__main__":
    main()
