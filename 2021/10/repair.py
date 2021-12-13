MATCHES = {")": "(", "]": "[", "}": "{", ">": "<"}
MATCHES.update({v: k for k, v in MATCHES.items()})
SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def autocomplete_score(line):
    stack = []
    for char in line:
        if char in "([{<":
            stack.append(char)
        elif stack[-1] == MATCHES[char]:
            stack.pop()
        else:
            # line is corrupted, use -1 as sentinel value
            return -1
    # line is not corrupted, calculate autocomplete score
    score = 0
    for char in reversed(stack):
        score = 5 * score + SCORES[MATCHES[char]]
    return score


def main():
    with open("nav_subsystem.txt") as f:
        scores = (autocomplete_score(line.strip()) for line in f)
        scores = sorted(s for s in scores if s != -1)
        print(scores[len(scores) // 2])


if __name__ == "__main__":
    main()
