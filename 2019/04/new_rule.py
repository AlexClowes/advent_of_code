def is_valid(n):
    digits = list(map(int, str(n)))
    digits.insert(0, digits[0] - 1)
    digits.append(digits[-1] + 1)
    return (
        all(d1 <= d2 for d1, d2 in zip(digits, digits[1:]))
        and any(d1 != d2 == d3 != d4 for d1, d2, d3, d4 in zip(*(digits[i:] for i in range(4))))
    )


def main():
    print(sum(is_valid(n) for n in range(367479, 893698)))


if __name__ == "__main__":
    main()
