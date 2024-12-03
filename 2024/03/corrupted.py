def main():
    with open("program.txt") as f:
        memory = f.read()

    pos = 0

    def inc(n=1):
        nonlocal pos
        pos += n

    def match(substr):
        if memory[pos : pos + len(substr)] == substr:
            inc(len(substr))
            return True
        return False

    def get_digit():
        ret = 0
        while pos < len(memory) and (digit := memory[pos]).isdigit():
            ret = 10 * ret + int(digit)
            inc()
        return ret

    total = 0
    while pos < len(memory):
        if (
            match("mul(")
            and (first := get_digit()) is not None
            and match(",")
            and (second := get_digit()) is not None
            and match(")")
        ):
            total += first * second
        else:
            pos += 1
    print(total)


if __name__ == "__main__":
    main()
