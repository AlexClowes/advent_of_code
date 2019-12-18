from computer import launch_int_code_computer


def main():
    with open("program.txt") as f:
        program = [int(n) for n in f.readline().strip().split(",")]
    program[0] = 2
    in_queue, out_queue = launch_int_code_computer(program)

    # Routines worked out by hand
    main_routine = "A,B,A,C,A,B,C,B,C,B\n"
    a_routine = "L,10,R,8,L,6,R,6\n"
    b_routine = "L,8,L,8,R,8\n"
    c_routine = "R,8,L,6,L,10,L,10\n"
    for routine in [main_routine, a_routine, b_routine, c_routine]:
        for char in routine:
            in_queue.put(ord(char))
    in_queue.put(ord("n"))
    in_queue.put(ord("\n"))

    for out in iter(out_queue.get, StopIteration):
        if out > 256:
            print(out)

    in_queue.put(StopIteration)


if __name__ == "__main__":
    main()
