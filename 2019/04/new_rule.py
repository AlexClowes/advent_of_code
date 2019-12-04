def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits[::-1]


def is_increasing(digits):
    return all(d1 <= d2 for d1, d2 in zip(digits, digits[1:]))


def double_digits(digits):
    for i in range(len(digits) - 1):
        if (
            digits[i] == digits[i + 1]
            and (i == 0 or digits[i - 1] != digits[i])
            and (i == len(digits) - 2 or digits[i + 2] != digits[i])
        ):
            return True
    return False


def is_valid(n):
    digits = get_digits(n)
    return is_increasing(digits) and double_digits(digits)


def main():
    print(sum(is_valid(n) for n in range(367479, 893698)))


if __name__ == "__main__":
    main()
