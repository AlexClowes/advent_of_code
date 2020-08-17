def main():
    # Count prime numbers in range(b0, c + 17, 17)
    b0 = 99 * 100 + 100000
    c = b0 + 17000

    h = 0
    for b in range(b0, c + 17, 17):
        for d in range(2, b):
            if b % d == 0:
                h += 1
                break
            if d * d > b:
                break
    print(h)


if __name__ == "__main__":
    main()
