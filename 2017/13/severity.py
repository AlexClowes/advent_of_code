def main():
    severity = 0
    with open("firewall.txt") as f:
        for line in f:
            depth, scanner_range = map(int, line.strip().split(": "))
            if depth % (2 * scanner_range - 2) == 0:
                severity += depth * scanner_range
    print(severity)


if __name__ == "__main__":
    main()
