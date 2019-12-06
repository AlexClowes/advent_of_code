def q(n):
    return (2 * n + 1) ** 2


def main():
    p = 289326
    n = 1
    while p > q(n):
        n += 1
    print(2 * n - (q(n) - p) % (2 * n))


if __name__ == "__main__":
    main()
