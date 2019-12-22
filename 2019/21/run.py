from computer import launch_int_code_computer


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]
    in_queue, out_queue = launch_int_code_computer(program)

    instructions = [
        "NOT E T",
        "NOT H J",
        "AND J T",
        "NOT T J",
        "AND D J",
        "NOT A T",
        "NOT T T",
        "AND B T",
        "AND C T",
        "NOT T T",
        "AND T J",
        "RUN",
    ]

    for char in "\n".join(instructions) + "\n":
        in_queue.put(ord(char))
    in_queue.put(StopIteration)
    output = "".join(
        chr(n) if n < 256 else str(n) for n in iter(out_queue.get, StopIteration)
    )
    print(output)


if __name__ == "__main__":
    main()
