def main():
    skip_size = 359

    pos = 0
    for i in range(5 * 10 ** 7 + 1):
        if pos == 0:
            ret = i
        pos = (pos + skip_size + 1) % (i + 1)
    print(ret)


if __name__ == "__main__":
    main()
