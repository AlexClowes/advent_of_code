def terminates(instructions):
    accumulator = 0
    seen = set()
    ip = 0
    while True:
        if ip == len(instructions):
            return True, accumulator
        if ip in seen or ip < 0 or ip > len(instructions):
            return False, accumulator
        seen.add(ip)
        operator, operand = instructions[ip].split()
        operand = int(operand)
        if operator == "jmp":
            ip += operand
        else:
            if operator == "acc":
                accumulator += operand
            ip += 1


def main():
    with open("program.txt") as f:
        instructions = [line.strip() for line in f]

    for i, line in enumerate(instructions):
        if "nop" in line:
            new_line = line.replace("nop", "jmp")
        elif "jmp" in line:
            new_line = line.replace("jmp", "nop")
        else:
            continue
        instructions[i] = new_line
        fixed, acc = terminates(instructions)
        if fixed:
            print(acc)
            break
        instructions[i] = line


if __name__ == "__main__":
    main()
