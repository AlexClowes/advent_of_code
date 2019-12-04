def match_sum(digits):
    digits.append(digits[0])
    return sum(d1 for d1, d2 in zip(digits, digits[1:]) if d1 == d2)


def main():
    with open("digits.txt") as f:
        digits = list(map(int, f.readline().strip()))
    print(match_sum(digits))


if __name__ == "__main__":
    main()
