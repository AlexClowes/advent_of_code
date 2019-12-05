def get_code(instructions):
    code = []
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    i, j = 1, 1
    for line in instructions:
        for char in line:
            if char == "U":
                i = max(0, i - 1)
            elif char == "D":
                i = min(2, i + 1)
            elif char == "L":
                j = max(0, j - 1)
            elif char == "R":
                j = min(2, j + 1)
        code.append(keypad[i][j])
    return "".join(str(n) for n in code)


def main():
    with open("instructions.txt") as f:
        instructions = [line.strip() for line in f]        
    print(get_code(instructions))


if __name__ == "__main__":
    main()
