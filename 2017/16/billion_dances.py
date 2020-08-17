from itertools import count


def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def main():
    programs = list("abcdefghijklmnop")

    def spin(n):
        nonlocal programs
        programs = programs[-n:] + programs[:-n]

    def exchange(i, j):
        programs[i], programs[j] = programs[j], programs[i]

    def partner(a, b):
        exchange(programs.index(a), programs.index(b))

    ops = {"s": spin, "x": exchange, "p": partner}

    with open("instructions.txt") as f:
        instructions = f.read().strip().split(",")

    def dance():
        for instr in instructions:
            ops[instr[0]](*map(try_int, instr[1:].split("/")))

    original_state = "".join(programs)
    for n in count(1):
        dance()
        if "".join(programs) == original_state:
            break
    for _ in range(10 ** 9 % n):
        dance()
    print("".join(programs))


if __name__ == "__main__":
    main()

