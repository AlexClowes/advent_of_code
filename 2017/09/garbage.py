def scan(stream):
    in_garbage = False
    pos = 0
    level = 0
    score = 0
    garbage_count = 0
    while pos < len(stream):
        if not in_garbage:
            if stream[pos] == "{":
                level += 1
            elif stream[pos] == "}":
                score += level
                level -= 1
            elif stream[pos] == "<":
                in_garbage = True
        else:
            if stream[pos] == "!":
                pos += 1
            elif stream[pos] == ">":
                in_garbage = False
            else:
                garbage_count += 1
        pos += 1
    return score, garbage_count


def main():
    with open("stream.txt") as f:
        score, garbage_count = scan(f.read().strip())
        print(score)
        print(garbage_count)


if __name__ == "__main__":
    main()
