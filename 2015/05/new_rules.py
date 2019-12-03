def is_nice(string):
    for i in range(len(string) - 1):
        substring = string[i : i + 2]
        if substring in string[i + 2:]:
            break
    else:
        return False

    spaced_repeat = any(c1 == c2 for c1, c2 in zip(string, string[2:]))
    if not spaced_repeat:
        return False

    return True


def main():
    with open("strings.txt") as f:
        print(sum(map(is_nice, f)))


if __name__ == "__main__":
    main()
