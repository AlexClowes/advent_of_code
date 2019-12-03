def is_nice(string):
    vowel_count = sum(string.count(v) for v in "aeiou")
    if vowel_count < 3:
        return False

    repeated_char = any(c1 == c2 for c1, c2 in zip(string, string[1:]))
    if not repeated_char:
        return False

    for bad_substring in ["ab", "cd", "pq", "xy"]:
        if bad_substring in string:
            return False

    return True


def main():
    with open("strings.txt") as f:
        print(sum(map(is_nice, f)))


if __name__ == "__main__":
    main()
