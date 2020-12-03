def main():
    with open("expenses.txt") as f:
        vals = set(int(line.strip()) for line in f)
    for v1 in vals:
        for v2 in vals:
            if 2020 - v1 - v2 in vals:
                print(v1 * v2 * (2020 - v1 - v2))
                return


if __name__ == "__main__":
    main()
