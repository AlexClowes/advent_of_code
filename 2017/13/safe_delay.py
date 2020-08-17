from itertools import count


def main():
    with open("firewall.txt") as f:
        firewall = [tuple(map(int, line.strip().split(": "))) for line in f]

    for t in count():
        if all(
            (t + depth) % (2 * scanner_range - 2) != 0
            for depth, scanner_range in firewall
        ):
            print(t)
            return


if __name__ == "__main__":
    main()
