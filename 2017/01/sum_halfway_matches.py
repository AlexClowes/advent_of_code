def halfway_match_sum(digits):
    l = len(digits)
    return sum(digits[i] for i in range(l) if digits[i] == digits[(i + l // 2) % l])


def main():
    with open("digits.txt") as f:
        digits = list(map(int, f.readline().strip()))
    print(halfway_match_sum(digits))


if __name__ == "__main__":
    main()
