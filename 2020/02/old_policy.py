import re


def is_valid(line):
    pat = r"(\d+)-(\d+) (\w): (\w+)"
    min_count, max_count, char, pword = re.match(pat, line).groups()
    return int(min_count) <= pword.count(char) <= int(max_count)


def main():
    with open("passwords.txt") as f:
        print(sum(is_valid(line.strip()) for line in f))


if __name__ == "__main__":
    main()
