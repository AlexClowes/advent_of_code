from run import run_program


def main():
    with open("program.txt") as f:
        program = list(map(int, f.readline().split(",")))
    program[1:3] = 12, 2
    print(run_program(program)[0])


if __name__ == "__main__":
    main()
