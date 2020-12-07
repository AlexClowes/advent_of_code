import collections
import re


def get_rules():
    rules = collections.defaultdict(list)
    with open("rules.txt") as f:
        for line in f:
            container, *contained = re.findall(r"(\w+ \w+) bag", line)
            for c in contained:
                rules[c].append(container)
    return rules


def main():
    rules = get_rules()

    # Traverse bag network, starting from shiny gold
    q = collections.deque(("shiny gold",))
    seen = set()
    while q:
        current_bag = q.popleft()
        for next_bag in rules[current_bag]:
            if next_bag not in seen:
                seen.add(next_bag)
                q.append(next_bag)
    print(len(seen))


if __name__ == "__main__":
    main()
