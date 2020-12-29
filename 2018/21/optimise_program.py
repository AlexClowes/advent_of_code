def main():
    """
    An optimised implementation of the program specified in the puzzle input.
    The program would terminate if registers[0] == registers[1] on line 28, so
    if registers[1] takes a value on line 28, then setting registers[0] to that
    value would cause the program to halt. So for part 2, we generate successive
    values of registers[1] until we get a repeat, then use the last value.
    """
    r1_vals = set()
    last_r1_val = None

    r1 = 8725355
    r2 = 65536
    while True:
        r1 = (r1 + (r2 & 255)) & 16777215
        r1 = (r1 * 65899) & 16777215
        if r2 >= 256:
            r2 //= 256
        else:
            if r1 in r1_vals:
                print(last_r1_val)
                break
            r1_vals.add(r1)
            last_r1_val = r1
            r2 = 65536 | r1
            r1 = 8725355


if __name__ == "__main__":
    main()
