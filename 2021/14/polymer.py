from collections import defaultdict


def main():
    with open("formula.txt") as f:
        template = f.readline().strip()
        f.readline()
        rules = dict(line.strip().split(" -> ") for line in f)

    def iterate(pairs):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            insertion = rules["".join(pair)]
            new_pairs[pair[0] + insertion] += count
            new_pairs[insertion + pair[1]] += count
        return new_pairs

    def evaluate(pairs):
        char_count = defaultdict(int)
        for pair, count in pairs.items():
            char_count[pair[0]] += count
        # Last character is always the same
        char_count[template[-1]] += 1
        return max(char_count.values()) - min(char_count.values())

    pairs = defaultdict(int)
    for pair in zip(template, template[1:]):
        pairs[pair] += 1

    for _ in range(10):
        pairs = iterate(pairs)
    print(evaluate(pairs))

    for _ in range(40 - 10):
        pairs = iterate(pairs)
    print(evaluate(pairs))


if __name__ == "__main__":
    main()
