def fib(n):
    if n <= 1:
        return n
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


def main():
    print(fib(28) + 196)
    print(fib(35) + 196)


if __name__ == "__main__":
    main()
