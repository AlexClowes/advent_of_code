from collections import defaultdict


def main():
    nums = []
    counts = defaultdict(int)
    with open("lists.txt") as f:
        for line in f:
            num1, num2 = map(int, line.strip().split("   "))
            nums.append(num1)
            counts[num2] += 1

    print(sum(n * counts[n] for n in nums))


if __name__ == "__main__":
    main()
