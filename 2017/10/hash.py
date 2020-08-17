from functools import reduce
from operator import xor


class CircList:
    def __init__(self, n):
        self.n = n
        self.vals = list(range(n))

    def __getitem__(self, idx):
        return self.vals[idx % self.n]

    def __setitem__(self, idx, val):
        self.vals[idx % self.n] = val


def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]


def to_hex(n):
    chars = "0123456789abcdef"
    return chars[n // 16] + chars[n % 16]


def hash(string):
    lengths = [ord(c) for c in string] + [17, 31, 73, 47, 23]

    pos = 0
    skip = 0
    cl = CircList(256)
    for _ in range(64):
        for l in lengths:
            for i in range(l // 2):
                swap(cl, pos + i, pos + l - i - 1)
            pos += l + skip
            skip += 1
    sparse_hash = cl.vals

    dense_hash = [reduce(xor, sparse_hash[i * 16 : (i + 1) * 16]) for i in range(16)]

    return "".join(map(to_hex, dense_hash))


def main():
    with open("lengths.txt") as f:
        print(hash(f.read().strip()))


if __name__ == "__main__":
    main()
