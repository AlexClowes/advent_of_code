import numpy as np

from computer import launch_int_code_computer


def adjacent(i, j):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]
    in_queue, out_queue = launch_int_code_computer(program)

    scaffolding_map = [[]]
    for char in map(chr, iter(out_queue.get, StopIteration)):
        if char == "\n":
            scaffolding_map.append([])
        else:
            scaffolding_map[-1].append(char)
    scaffolding_map = np.array([np.array(line) for line in scaffolding_map if line])

    alignment_sum = 0
    for i in range(1, scaffolding_map.shape[0] - 1):
        for j in range(1, scaffolding_map.shape[1] - 1):
            if (
                scaffolding_map[i, j] == "#"
                and all(scaffolding_map[adj] == "#" for adj in adjacent(i, j))
            ):
                alignment_sum += i * j
    print(alignment_sum)

    in_queue.put(StopIteration)


if __name__ == "__main__":
    main()
