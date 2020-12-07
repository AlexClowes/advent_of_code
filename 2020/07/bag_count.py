import collections
import re


def get_rules():
    rules = collections.defaultdict(list)
    with open("rules.txt") as f:
        for line in f:
            container = re.match(r"(\w+ \w+) bags contain", line).group(1)
            contained = [
                (int(count), colour)
                for count, colour in re.findall(r"(\d) (\w+ \w+) bag", line)
            ]
            rules[container] = contained
    return rules


def main():
    rules = get_rules()

    def tree_weight(colour):
        return 1 + sum(
            count * tree_weight(new_colour) for count, new_colour in rules[colour]
        )

    print(tree_weight("shiny gold") - 1)


if __name__ == "__main__":
    main()
