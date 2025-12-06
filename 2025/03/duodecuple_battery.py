def max_joltage(battery_bank, size):
    if size == 0:
        return ""
    for digit in "987654321":
        for idx, first in enumerate(battery_bank[: len(battery_bank) - size + 1]):
            if first == digit:
                return first + max_joltage(battery_bank[idx + 1 :], size - 1)


def main():
    with open("batteries.txt") as f:
        print(sum(int(max_joltage(line.strip(), 12)) for line in f))


if __name__ == "__main__":
    main()
