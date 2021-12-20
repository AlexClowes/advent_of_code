from functools import reduce
from itertools import permutations
from operator import add


class SailFishNumber:
    @classmethod
    def from_str_rep(cls, str_rep):
        def gen_num_depth_pairs():
            depth = -1
            for char in str_rep:
                if char == "[":
                    depth += 1
                elif char == "]":
                    depth -= 1
                elif char != ",":
                    yield [int(char), depth]
        return cls(gen_num_depth_pairs())

    def __init__(self, pairs):
        self.pairs = list(pairs)
        while self._explode() or self._split():
            pass

    def __add__(self, other):
        return SailFishNumber([v, d + 1] for v, d in self.pairs + other.pairs)

    def _explode(self):
        try:
            idx = next(idx for idx, (_, depth) in enumerate(self.pairs) if depth == 4)
        except StopIteration:
            return False
        # Left
        if idx > 0:
            self.pairs[idx - 1][0] += self.pairs[idx][0]
        # Right
        if idx < len(self.pairs) - 2:
            self.pairs[idx + 2][0] += self.pairs[idx + 1][0]
        # Remove exploded pair
        self.pairs[idx] = [0, self.pairs[idx][1] - 1]
        del self.pairs[idx + 1]
        return True

    def _split(self):
        try:
            idx = next(idx for idx, (val, _) in enumerate(self.pairs) if val >= 10)
        except StopIteration:
            return False
        val, depth = self.pairs[idx]
        self.pairs[idx] = [val // 2, depth + 1]
        self.pairs.insert(idx + 1, [val - val // 2, depth + 1])
        return True

    def as_tree(self):
        stack = []
        for val, depth in self.pairs:
            while stack and stack[-1][1] == depth:
                val = [stack.pop()[0], val]
                depth -= 1
            stack.append((val, depth))
        return stack[0][0]

    def magnitude(self):
        def mag(tree):
            if isinstance(tree, int):
                return tree
            return 3 * mag(tree[0]) + 2 * mag(tree[1])
        return mag(self.as_tree())


def main():
    with open("homework.txt") as f:
        numbers = [SailFishNumber.from_str_rep(line.strip()) for line in f]

    # Part 1
    print(reduce(add, numbers).magnitude())
    # Part 2
    print(max((x + y).magnitude() for x, y in permutations(numbers, 2)))


if __name__ == "__main__":
    main()
