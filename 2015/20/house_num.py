from itertools import count


def sum_factors(n):
    ret = 1
    p = 2
    while p * p <= n:
        product_term = 1
        while n % p == 0:
            n //= p
            product_term = p * product_term + 1
        ret *= product_term
        p += 1
    if n > 1:
        ret *= (1 + n)
    return ret


def main():
    step = 2 * 2 * 2 * 3 * 3 * 5
    for n in count(step, step):
        if sum_factors(n) >= 3600000:
            print(n)
            break


if __name__ == "__main__":
    main()
