from itertools import zip_longest
from queue import Queue
from threading import Thread

from computer import int_code_computer


def grouper(n, iterable):
    args = [iter(iterable)] * n
    return zip_longest(*args)


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]
    program[0] = 2

    input_queue = Queue()
    output_queue = Queue()
    Thread(target=int_code_computer, args=(program, input_queue, output_queue)).start()

    paddle_pos, ball_pos, score = 0, 0, 0
    screen = [[" "] * 38 for _ in range(21)]
    for x, y, tile in grouper(3, iter(output_queue.get, StopIteration)):
        if x == -1 and y == 0:
            score = tile
        else:
            screen[y][x] = " #%_o"[tile]
            if screen[y][x] == "_":
                paddle_pos = x
            elif screen[y][x] == "o":
                ball_pos = x
                input_queue.put(sign(ball_pos - paddle_pos))
        #time.sleep(0.005)
        #print("\n".join("".join(line) for line in screen))
    print(score)


if __name__ == "__main__":
    main()
