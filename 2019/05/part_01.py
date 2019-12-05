from run import run


def main():
    with open("program.txt") as f:
        program = list(map(int, f.readline().split(",")))
    run(program, 1)


if __name__ == "__main__":
    main()
