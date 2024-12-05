from itertools import takewhile


def check(update, rules):
    for first, second in rules:
        if (
            first in update
            and second in update
            and update.index(first) > update.index(second)
        ):
            return False
    return True


def median(update):
    assert len(update) % 2 == 1
    return update[len(update) // 2]


def main():
    with open("print_orders.txt") as f:
        rule_lines = takewhile(bool, (line.strip() for line in f))
        rules = [line.split("|") for line in rule_lines]
        updates = [line.strip().split(",") for line in f]

    print(sum(int(median(update)) for update in updates if check(update, rules)))



if __name__ == "__main__":
    main()
