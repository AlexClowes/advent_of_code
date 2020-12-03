import re


def is_valid(line):
    pat = r"(\d+)-(\d+) (\w): (\w+)"
    pos1, pos2, char, pword = re.match(pat, line).groups()
    pos1, pos2 = int(pos1), int(pos2)
    return (pword[pos1 - 1] == char) ^ (pword[pos2 - 1] == char)


def main():
    with open("passwords.txt") as f:
        print(sum(is_valid(line.strip()) for line in f))


if __name__ == "__main__":
    main()
