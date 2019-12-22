from computer import launch_int_code_computer


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]
    in_queue, out_queue = launch_int_code_computer(program)

    instructions = [
        "NOT A T",
        "NOT B J",
        "OR T J",
        "NOT C T",
        "OR T J",
        "AND D J",
        "WALK",
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
