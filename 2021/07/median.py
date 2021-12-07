from statistics import median


def main():
    with open("crabs.txt") as f:
        positions = [int(x) for x in f.read().split(",")]
    med = int(median(positions))
    print(sum(abs(pos - med) for pos in positions))



if __name__ == "__main__":
    main()
