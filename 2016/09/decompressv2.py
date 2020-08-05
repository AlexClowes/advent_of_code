import re


def decompressed_len(string):
    if string:
        m = re.match(r"\((\d+)x(\d+)\)", string)
        if m:
            length, repeats = map(int, m.groups())
            mlen = len(m.group(0))
            return (
                repeats * decompressed_len(string[mlen:mlen+length])
                + decompressed_len(string[mlen + length:])
            )
        else:
            return 1 + decompressed_len(string[1:])
    return 0


def main():
    with open("message.txt") as f:
        print(decompressed_len(f.read().strip()))


if __name__ == "__main__":
    main()
