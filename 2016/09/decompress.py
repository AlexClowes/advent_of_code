import re


def decompressed_len(string):
    pat = r"\((\d+)x(\d+)\)"
    i = 0
    ret = 0
    while i < len(string):
        m = re.match(pat, string[i:])
        if m:
            #import pdb; pdb.set_trace()
            length, repeats = map(int, m.groups())
            ret += length * repeats
            i += m.end() + length
        else:
            ret += 1
            i += 1
    return ret


def main():
    with open("message.txt") as f:
        print(decompressed_len(f.read().strip()))


if __name__ == "__main__":
    main()
