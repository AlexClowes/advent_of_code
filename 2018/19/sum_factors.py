def sum_factors(n):
    ret = 0
    divisor = 1
    while divisor * divisor < n:
        if n % divisor == 0:
            ret += divisor
            ret += (n // divisor)
        divisor += 1
    if n % divisor == 0:
        ret += divisor
    return ret


def main():
    # After simplifying program by hand...
    print(sum_factors(998))
    print(sum_factors(10551398))


if __name__ == "__main__":
    main()
