MATCHES = {")": "(", "]": "[", "}": "{", ">": "<"}
SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}


def corruption_score(line):
    stack = []
    for char in line:
        if char in "([{<":
            stack.append(char)
        elif stack[-1] == MATCHES[char]:
            stack.pop()
        else:
            return SCORES[char]
    return 0


def main():
    with open("nav_subsystem.txt") as f:
        print(sum(corruption_score(line.strip()) for line in f))


if __name__ == "__main__":
    main()
