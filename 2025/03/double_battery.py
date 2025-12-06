def max_joltage(battery_bank):
    for digit in "987654321":
        for idx, first in enumerate(battery_bank[:-1]):
            if first == digit:
                second = max(battery_bank[idx + 1 :])
                return int(first + second)


def main():
    with open("batteries.txt") as f:
        print(sum(max_joltage(line.strip()) for line in f))


if __name__ == "__main__":
    main()
