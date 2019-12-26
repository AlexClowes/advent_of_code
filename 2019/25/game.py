from computer import launch_int_code_computer


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]

    in_queue, out_queue = launch_int_code_computer(program)

    try:
        while True:
            output = "".join(chr(n) for n in iter(out_queue.get, ord("\n")))
            if output == "Command?":
                for char in input("Command? >"):
                    in_queue.put(ord(char))
                in_queue.put(ord("\n"))
            else:
                print(output)
    finally:
        in_queue.put(StopIteration)


if __name__ == "__main__":
    main()
