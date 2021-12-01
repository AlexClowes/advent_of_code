def main():
    with open("report.txt") as f:
        depths = [int(line) for line in f]
    print(sum(d1 < d2 for d1, d2 in zip(depths, depths[1:])))
    print(sum(d1 < d2 for d1, d2 in zip(depths, depths[3:])))


if __name__ == "__main__":
    main()
