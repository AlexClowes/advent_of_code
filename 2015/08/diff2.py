def diff(string):
    total = 2
    for char in string:
        if char in ("\"", "\\"):
            total += 1
    return total


def main():
    with open("strings.txt") as f:
        lines = (l.strip() for l in f.readlines())

    print(sum(diff(l) for l in lines))


if __name__ == "__main__":
    main()
