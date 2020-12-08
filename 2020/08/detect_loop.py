def catch_loop(instructions):
    accumulator = 0
    seen = set()
    ip = 0
    while ip not in seen:
        seen.add(ip)
        operator, operand = instructions[ip].split()
        operand = int(operand)
        if operator == "jmp":
            ip += operand
        else:
            if operator == "acc":
                accumulator += operand
            ip += 1
    return accumulator


def main():
    with open("program.txt") as f:
        instructions = [line.strip() for line in f]
    print(catch_loop(instructions))


if __name__ == "__main__":
    main()
