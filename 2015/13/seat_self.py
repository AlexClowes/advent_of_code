from collections import defaultdict
from itertools import permutations
import re


def get_names_and_happiness_change(line):
    search_pat = r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."
    name1, gain_lose, magnitude, name2 = re.match(search_pat, line).groups()
    sign = 1 if gain_lose == "gain" else -1
    return name1, name2, sign * int(magnitude)


def main():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    lookup = defaultdict(dict)
    for line in lines:
        name1, name2, change = get_names_and_happiness_change(line.strip())
        lookup[name1][name2] = change

    # Add self to lookup table
    for name in list(lookup.keys()):
        lookup["me"][name] = lookup[name]["me"] = 0

    def score_perm(p):
        ret = 0
        for pos, name in enumerate(p):
            adj = p[(pos + 1) % len(p)]
            ret += lookup[name][adj] + lookup[adj][name]
        return ret

    print(max(score_perm(p) for p in permutations(lookup.keys())))




if __name__ == "__main__":
    main()



