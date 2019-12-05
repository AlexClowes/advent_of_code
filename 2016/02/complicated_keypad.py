def get_code(instructions):
    code = []
    keypad = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, "A", "B", "C", 0],
        [0, 0, "D", 0, 0],
    ]
    i, j = 2, 0
    for line in instructions:
        for char in line:
            if char == "U" and i > 0 and keypad[i - 1][j] != 0:
                i -= 1
            elif char == "D" and i < 4 and keypad[i + 1][j] != 0:
                i += 1
            elif char == "L" and j > 0 and keypad[i][j - 1] != 0:
                j -= 1
            elif char == "R" and j < 4 and keypad[i][j + 1] != 0:
                j += 1
        code.append(keypad[i][j])
    return "".join(str(n) for n in code)


def main():
    with open("instructions.txt") as f:
        instructions = [line.strip() for line in f]        
    print(get_code(instructions))


if __name__ == "__main__":
    main()
