from run import IntCodeComputer


def main():
    with open("program.txt") as f:
        program = list(map(int, f.readline().split(",")))
    IntCodeComputer(program).run(5)


if __name__ == "__main__":
    main()
