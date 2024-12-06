SNAFU2DEC = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
DEC2SNAFU = {v: k for k, v in SNAFU2DEC.items()}


def snafu_to_decimal(snafu):
    ret = 0
    for char in snafu:
        ret *= 5
        ret += SNAFU2DEC[char]
    return ret


def decimal_to_snafu(decimal):
    ret = ""
    while decimal:
        decimal, r = divmod(decimal, 5)
        r = (r + 2) % 5 - 2
        decimal += r < 0
        ret = DEC2SNAFU[r] + ret
    return ret


def main():
    with open("nos.txt") as f:
        print(decimal_to_snafu(sum(snafu_to_decimal(line.strip()) for line in f)))


if __name__ == "__main__":
    main()
