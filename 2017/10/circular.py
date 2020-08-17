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


def main():
    with open("lengths.txt") as f:
        lengths = map(int, f.read().strip().split(","))
    cl = CircList(256)

    pos = 0
    skip = 0
    for l in lengths:
        for i in range(l // 2):
            swap(cl, pos + i, pos + l - i - 1)
        pos += l + skip
        skip += 1
    print(cl[0] * cl[1])


if __name__ == "__main__":
    main()
