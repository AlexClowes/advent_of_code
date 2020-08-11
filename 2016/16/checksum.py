def dragon(s):
    return s + "0" + "".join("0" if c == "1" else "1" for c in s[::-1])


def checksum(s):
    reduced = "".join("01"[c1 == c2] for c1, c2 in zip(s[::2], s[1::2]))
    return reduced if len(reduced) % 2 == 1 else checksum(reduced)


def main():
    for length in (272, 35651584):
        s = "10111100110001111"
        while len(s) < length:
            s = dragon(s)
        print(checksum(s[:length]))


if __name__ == "__main__":
    main()
