from itertools import zip_longest
from queue import Queue

from computer import int_code_computer


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]

    output_queue = Queue()
    c = int_code_computer(program, Queue(), output_queue)
    outputs = iter(output_queue.get, StopIteration)
    print(sum(tile == 2 for _, _, tile in grouper(3, outputs, fillvalue=None)))


if __name__ == "__main__":
    main()
