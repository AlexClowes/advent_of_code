from computer import launch_int_code_computer


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]

    def in_beam(x, y):
        in_queue, out_queue = launch_int_code_computer(program)
        in_queue.put(x)
        in_queue.put(y)
        return out_queue.get()

    print(sum(in_beam(x, y) for x in range(50) for y in range(50)))


if __name__ == "__main__":
    main()
