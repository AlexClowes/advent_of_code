from run import run_program


def main():
    with open("program.txt") as f:
        program = list(map(int, f.readline().split(",")))
    for noun in range(100):
        for verb in range(100):
            prog_copy = list(program)
            prog_copy[1:3] = noun, verb
            if run_program(prog_copy)[0] == 19690720:
                print(100 * noun + verb)


if __name__ == "__main__":
    main()
