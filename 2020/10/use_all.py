def main():
    with open("adapters.txt") as f:
        adapters = sorted(int(line.strip()) for line in f)

    diffs = (a2 - a1 for a1, a2 in zip(adapters[:-1], adapters[1:]))
    count_1 = adapters[0] == 1
    count_3 = 1 + (adapters[0] == 3)
    for d in diffs:
        if d == 1:
            count_1 += 1
        elif d == 3:
            count_3 += 1
    print(count_1 * count_3)


if __name__ == "__main__":
    main()
