def f(n):
    if n == 1:
        return 1
    return 2 * (f(n // 2) + n % 2) - 1


def main():
    print(f(3018458))


if __name__ == "__main__":
    main()
