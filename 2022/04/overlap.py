class Range:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi

    def __repr__(self):
        return f"{self.__class__.__name__}({self.lo}, {self.hi})"

    def overlap(self, other):
        return self.lo <= other.hi and other.lo <= self.hi

    @classmethod
    def from_str(cls, range_str):
        return cls(*map(int, range_str.split("-")))


def main():
    with open("work_detail.txt") as f:
        range_pairs = (
            tuple(map(Range.from_str, line.strip().split(","))) for line in f
        )
        print(sum(r1.overlap(r2) for r1, r2 in range_pairs))


if __name__ == "__main__":
    main()
