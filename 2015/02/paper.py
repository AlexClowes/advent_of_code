def paper(a, b, c):
    return 2 * (a * b + b * c + c * a) + (a * b * c) // max(a, b, c)


def main():
    with open("dimensions.txt") as f:
        dims = (map(int, line.split("x")) for line in f)
        print(sum(paper(*d) for d in dims))


if __name__ == "__main__":
    main()
