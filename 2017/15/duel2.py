from itertools import islice


def generator(start, factor, divisor):
    x = start
    while True:
        x = (x * factor) % 2147483647
        if x % divisor == 0:
            yield x & 0xffff


def main():
    gen_A = generator(679, 16807, 4)
    gen_B = generator(771, 48271, 8)

    print(sum(ga == gb for ga, gb in islice(zip(gen_A, gen_B), 5 * 10 ** 6)))


if __name__ == "__main__":
    main()
