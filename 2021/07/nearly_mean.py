from math import ceil, floor


def fuel_cost(x, y):
    d = abs(x - y)
    return d * (d + 1) // 2


def main():
    with open("crabs.txt") as f:
        positions = [int(x) for x in f.read().split(",")]

    mean = sum(positions) / len(positions)
    # Optimal point is integer in range [mean - 1/2, mean + 1/2]
    min_sum = min(
        sum(fuel_cost(x, pos) for pos in positions)
        for x in (int(mean) - 1, int(mean), int(mean) + 1)
    )
    print(min_sum)



if __name__ == "__main__":
    main()
