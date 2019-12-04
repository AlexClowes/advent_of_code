def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits[::-1]


def is_valid(n):
    digits = get_digits(n)
    return (
        all(d1 <= d2 for d1, d2 in zip(digits, digits[1:]))
        and any(d1 == d2 for d1, d2 in zip(digits, digits[1:]))
    )


def main():
    print(sum(is_valid(n) for n in range(367479, 893698)))


if __name__ == "__main__":
    main()
