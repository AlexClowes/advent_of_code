from itertools import combinations


def product(iterable):
    ret = 1
    for el in iterable:
        ret *= el
    return ret


def gen_groups(target, weights):
    for i in range(1, len(weights) + 1):
        candidates = (comb for comb in combinations(weights, i) if sum(comb) == target)
        yield from sorted(candidates, key=product)


def main():
    with open("weights.txt") as f:
        weights = [int(line.strip()) for line in f][::-1]
    weights = weights
    target_weight = sum(weights) // 4

    group1_candidates = gen_groups(target_weight, weights)
    for group1 in group1_candidates:
        unused = [w for w in weights if w not in group1]  # Assumes no duplicate weights
        for group2 in gen_groups(target_weight, unused):
            still_unused = [w for w in unused if w not in group2]
            for group3 in gen_groups(target_weight, still_unused):
                # If group 3 exists, then so does group 4 and we are done
                print(product(group1))
                return


if __name__ == "__main__":
    main()
