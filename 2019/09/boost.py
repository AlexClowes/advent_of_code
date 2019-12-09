from computer import int_code_computer


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.read().strip().split(",")]

    c = int_code_computer(program)
    print(c.send(1))

    c = int_code_computer(program)
    print(c.send(2))


if __name__ == "__main__":
    main()
