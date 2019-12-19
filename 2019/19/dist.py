from computer import launch_int_code_computer


def in_beam(program, x, y):
    in_queue, out_queue = launch_int_code_computer(program)
    in_queue.put(x)
    in_queue.put(y)
    return out_queue.get()


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]

    x, y = 900, 900
    while True:
        if in_beam(program, x, y):
            if in_beam(program, x + 99, y - 99):
                break
            else:
                y += 1
        else:
            x += 1
    print(10 ** 4 * x + y - 99)


if __name__ == "__main__":
    main()
