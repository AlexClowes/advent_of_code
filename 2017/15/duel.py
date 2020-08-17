from itertools import islice


def generator(start, factor):
    x = start
    while True:
        x = (x * factor) % 2147483647
        yield x & 0xffff


def main():
    gen_A = generator(679, 16807)
    gen_B = generator(771, 48271)

    print(sum(ga == gb for ga, gb in islice(zip(gen_A, gen_B), 4 * 10 ** 7)))


if __name__ == "__main__":
    main()
